from torchbenchmark.util.framework.huggingface.model_factory import HuggingFaceModel
from torchbenchmark.tasks import SPEECH
import torch

class Model(HuggingFaceModel):
    task = SPEECH.RECOGNITION
    DEFAULT_EVAL_BSIZE = 8
    
    def __init__(self, test, device, jit=False, batch_size=None, extra_args=[]):
        super().__init__(name="hf_Whisper", test=test, device=device, jit=jit, batch_size=batch_size, extra_args=extra_args)
        self.feature_size = 80
        self.sequence_length = 3000
        self.input_features = torch.randn(size=(self.batch_size, self.feature_size, self.sequence_length),device=self.device).half()
        self.example_inputs = {"input_features": self.input_features.to(self.device), "input_ids" : self.input_features.to(self.device)}
        self.model.to(self.device)

    def train(self):
        raise NotImplementedError("Training is not implemented.")

