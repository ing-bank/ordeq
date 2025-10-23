from pathlib import Path

from config.batch_prediction_config import BatchPredictionConfig
from config.deployment_config import DeploymentConfig
from config.model_config import ModelConfig
from config.model_evaluation_config import ModelEvaluationConfig
from config.real_time_prediction_config import RealTimePredictionConfig
from ordeq import IO
from ordeq_common import Literal
from ordeq_files import Pickle
from ordeq_matplotlib import MatplotlibFigure
from torchvision import datasets

DATA_DIR = Path(__file__).parent.parent.parent / "data"
RAW_DATA_DIR = DATA_DIR / "01_raw"


# configurations
model_config = Literal(ModelConfig())
model_evaluation_config = Literal(ModelEvaluationConfig())
deployment_config = Literal(DeploymentConfig())
batch_prediction_config = Literal(BatchPredictionConfig())
real_time_prediction_config = Literal(RealTimePredictionConfig())

validation_split = Literal(0.2)
random_seed = Literal(42)

# raw data loading
train_dataset = Literal(
    datasets.MNIST(root=str(RAW_DATA_DIR), train=True, download=True)
)
test_dataset = Literal(
    datasets.MNIST(root=str(RAW_DATA_DIR), train=False, download=True)
)
raw_data = IO()
mnist_moments = Literal((0.1307, 0.3081))  # mean and std for MNIST

# preprocessing
processed_data = IO()
data_metadata = IO()

# training
training_device = IO()
training_metadata = IO()
train_loader = IO()
val_loader = IO()

# models
model = Pickle(path=Path(DATA_DIR / "02_models" / "mnist_cnn_model.pkl"))
# for this example we select the latest model as production model
production_model = Pickle(path=Path(DATA_DIR / "02_models" / "mnist_cnn_model.pkl"))

# evaluation
test_loader = IO()
model_evaluation_result = IO()
model_evaluation_metadata = IO()
confusion_matrix = MatplotlibFigure(
    path=Path(DATA_DIR / "03_reports" / "confusion_matrix.png")
)

# inference
inference_device = IO()
dummy_images = IO()
batch_predictions = IO()
batch_prediction_metadata = IO()
dummy_batch = IO()
real_time_predictions = IO()
real_time_prediction_metadata = IO()
