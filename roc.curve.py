"""
ROC Curve Analysis for SETI Signal Classification
Provides tools for evaluating machine learning models on SETI data using ROC curves.
"""
import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_curve, auc, plot_roc_curve, confusion_matrix
from sklearn.preprocessing import StandardScaler
import pandas as pd
import logging
from typing import Tuple, Dict, Any

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class SETIModelEvaluator:
    """Evaluate machine learning models for SETI signal classification."""
    
    def __init__(self):
        self.models = {}
        self.results = {}
    
    def prepare_sample_data(self, n_samples: int = 1000) -> Tuple[np.ndarray, np.ndarray]:
        """
        Generate sample SETI-like data for demonstration.
        In practice, this would load real SETI data.
        """
        np.random.seed(42)
        
        # Simulate features like frequency, intensity, signal duration, etc.
        X = np.random.randn(n_samples, 8)  # 8 features
        
        # Add some signal-like patterns
        signal_mask = np.random.rand(n_samples) < 0.1  # 10% signals
        X[signal_mask, 0] *= 3  # Stronger frequency component
        X[signal_mask, 1] += 2  # Higher intensity
        
        y = signal_mask.astype(int)  # Binary: 0=noise, 1=potential signal
        
        return X, y
    
    def setup_models(self) -> Dict[str, Any]:
        """Initialize machine learning models for comparison."""
        models = {
            'Random Forest': RandomForestClassifier(n_estimators=100, random_state=42),
            'SVM (RBF)': SVC(kernel='rbf', probability=True, random_state=42),
            'SVM (Linear)': SVC(kernel='linear', probability=True, random_state=42)
        }
        
        self.models = models
        return models
    
    def evaluate_models(self, X: np.ndarray, y: np.ndarray, test_size: float = 0.3) -> Dict:
        """
        Train and evaluate all models, generate ROC curves.
        
        Args:
            X: Feature matrix
            y: Target labels
            test_size: Proportion of data for testing
            
        Returns:
            Dictionary with evaluation results
        """
        try:
            # Split the data
            X_train, X_test, y_train, y_test = train_test_split(
                X, y, test_size=test_size, random_state=42, stratify=y
            )
            
            # Scale features for SVM
            scaler = StandardScaler()
            X_train_scaled = scaler.fit_transform(X_train)
            X_test_scaled = scaler.transform(X_test)
            
            # Setup plot
            plt.figure(figsize=(12, 8))
            
            results = {}
            
            for name, model in self.models.items():
                logger.info(f"Training {name}...")
                
                # Use scaled data for SVM, original for Random Forest
                if 'SVM' in name:
                    model.fit(X_train_scaled, y_train)
                    y_proba = model.predict_proba(X_test_scaled)[:, 1]
                    y_pred = model.predict(X_test_scaled)
                else:
                    model.fit(X_train, y_train)
                    y_proba = model.predict_proba(X_test)[:, 1]
                    y_pred = model.predict(X_test)
                
                # Calculate ROC curve
                fpr, tpr, _ = roc_curve(y_test, y_proba)
                roc_auc = auc(fpr, tpr)
                
                # Plot ROC curve
                plt.plot(fpr, tpr, linewidth=2, alpha=0.8,
                        label=f'{name} (AUC = {roc_auc:.3f})')
                
                # Store results
                results[name] = {
                    'auc': roc_auc,
                    'fpr': fpr,
                    'tpr': tpr,
                    'confusion_matrix': confusion_matrix(y_test, y_pred),
                    'model': model
                }
                
                logger.info(f"{name} - AUC: {roc_auc:.3f}")
            
            # Finalize ROC plot
            plt.plot([0, 1], [0, 1], 'k--', alpha=0.5)
            plt.xlim([0.0, 1.0])
            plt.ylim([0.0, 1.05])
            plt.xlabel('False Positive Rate', fontsize=12)
            plt.ylabel('True Positive Rate', fontsize=12)
            plt.title('ROC Curves - SETI Signal Classification Models', fontsize=14, pad=20)
            plt.legend(loc="lower right", fontsize=10)
            plt.grid(True, alpha=0.3)
            plt.tight_layout()
            
            # Save plot
            plt.savefig('seti_roc_curves.png', dpi=300, bbox_inches='tight')
            logger.info("ROC curves saved as 'seti_roc_curves.png'")
            
            plt.show()
            
            self.results = results
            return results
            
        except Exception as e:
            logger.error(f"Error in model evaluation: {e}")
            return {}
    
    def print_detailed_results(self) -> None:
        """Print detailed evaluation results."""
        if not self.results:
            logger.warning("No results available. Run evaluate_models() first.")
            return
        
        print("\n" + "="*60)
        print("SETI SIGNAL CLASSIFICATION - MODEL COMPARISON")
        print("="*60)
        
        for name, result in self.results.items():
            print(f"\n{name}:")
            print(f"  AUC Score: {result['auc']:.4f}")
            
            cm = result['confusion_matrix']
            print(f"  Confusion Matrix:")
            print(f"    TN: {cm[0,0]}, FP: {cm[0,1]}")
            print(f"    FN: {cm[1,0]}, TP: {cm[1,1]}")
            
            # Calculate additional metrics
            precision = cm[1,1] / (cm[1,1] + cm[0,1]) if (cm[1,1] + cm[0,1]) > 0 else 0
            recall = cm[1,1] / (cm[1,1] + cm[1,0]) if (cm[1,1] + cm[1,0]) > 0 else 0
            f1 = 2 * (precision * recall) / (precision + recall) if (precision + recall) > 0 else 0
            
            print(f"  Precision: {precision:.4f}")
            print(f"  Recall: {recall:.4f}")
            print(f"  F1-Score: {f1:.4f}")

def main():
    """Main function to run SETI model evaluation."""
    logger.info("Starting SETI Model Evaluation...")
    
    # Initialize evaluator
    evaluator = SETIModelEvaluator()
    
    # Setup models
    evaluator.setup_models()
    logger.info(f"Initialized {len(evaluator.models)} models")
    
    # Generate sample data (replace with real SETI data loading)
    X, y = evaluator.prepare_sample_data(n_samples=2000)
    logger.info(f"Generated sample data: {X.shape[0]} samples, {X.shape[1]} features")
    logger.info(f"Signal ratio: {y.sum()}/{len(y)} ({100*y.mean():.1f}%)")
    
    # Evaluate models
    results = evaluator.evaluate_models(X, y)
    
    if results:
        evaluator.print_detailed_results()
        
        # Find best model
        best_model = max(results.items(), key=lambda x: x[1]['auc'])
        print(f"\nBest Model: {best_model[0]} (AUC: {best_model[1]['auc']:.4f})")
    
    logger.info("SETI Model Evaluation completed!")

if __name__ == "__main__":
    main() 
