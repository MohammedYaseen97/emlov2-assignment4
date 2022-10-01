from torch import nn
import timm


class TimmNet(nn.Module):
    def __init__(
        self,
        model_name: str = 'densenet121',
        output_size: int = 10,
    ):
        super().__init__()

        self.model = timm.create_model(model_name, pretrained=True, num_classes=output_size)

    def forward(self, x):
        batch_size, channels, width, height = x.size()

        # (batch, 1, width, height) -> (batch, 1*width*height)
        # x = x.view(batch_size, -1)

        return self.model(x)


if __name__ == "__main__":
    _ = TimmNet()
