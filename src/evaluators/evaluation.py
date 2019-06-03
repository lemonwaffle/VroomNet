"""
Module that contains any functions relating to evaluation and the
Evaluator object (plotting, calculating statistics etc.)
"""
import numpy as np
from sklearn.metrics import precision_recall_fscore_support

from src.utils import factory


def eval_model(model, gen):
    """Evaluates a model based on the validation/test data generator.

    Args:
        model (BaseModel): Model to evaluate.
        gen (DataGenerator): Data generator to evaluate on.

    Returns:
        (precision, recall, fscore)
    """
    # Make sure generator is not shuffled?
    y_true = gen.classes
    predictions = model.predict_generator(gen)
    y_pred = np.argmax(predictions, axis=1)

    precision, recall, fscore, _ = \
        precision_recall_fscore_support(y_true, y_pred, average='micro')

    return precision, recall, fscore


# Creates the Evaluator object from the JSON config file path.
def create_evaluator(json_file):
    """Takes in the path of the JSON config file.

    Returns the Evaluator object created.
    """
    config = process_config(args.config)

    # Initialize the Data Loader
    data_loader = factory.create("src.dataloader."+config.data_loader.name)(config)
    # Initialize the Model (specifying weights)
    model = factory.create("src.models."+config.model.name)(config)
    # Initialize the Evaluator
    evaluator = factor.create("src.evaluators."+config.evaluator.name)(
        model.model,
        data_loader,
        config,
    )

    return evaluator
