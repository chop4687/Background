import torch
from model import MattingNetwork

model = MattingNetwork('resnet50').eval().cuda()
model.load_state_dict(torch.load('rvm_resnet50.pth'))  # or "resnet50asdfsadf"mobilenetv3

from inference import convert_video

convert_video(
    model,                           # The model, can be on any device (cpu or cuda).
    input_source='DANCE.mp4',        # A video file or an image sequence directory.
    output_type='video',             # Choose "video" or "png_sequence"
    output_composition='DANCE_com.mp4',    # File path if video; directory path if png sequence.
    output_alpha="DANCE_pha.mp4",          # [Optional] Output the raw alpha prediction.
    output_foreground="DANCE_fgr.mp4",     # [Optional] Output the raw foreground prediction.
    output_video_mbps=4,             # Output video mbps. Not needed for png sequence.
    downsample_ratio=1,           # A hyperparameter to adjust or use None for auto.
    seq_chunk=1,                    # Process n frames at once for better parallelism.
)

'''
from torch.utils.data import DataLoader
from torchvision.transforms import ToTensor
from inference_utils import VideoReader, VideoWriter
from PIL import Image
reader = VideoReader('tony_input.mp4', transform=ToTensor())
writer = VideoWriter('tony_output.mp4', frame_rate=30)

#bg = Image.open('bgr.png').convert('RGB')
#tt = ToTensor()
#bgr = tt(bg).cuda()

#bgr = torch.tensor([.47, 1, .6]).view(3, 1, 1).cuda()  # Green background.
bgr = torch.tensor([0, 1, 0]).view(3, 1, 1).cuda()  # Green background.
rec = [None] * 4                                       # Initial recurrent states.
downsample_ratio = 0.6                                # Adjust based on your video.

with torch.no_grad():
    for src in DataLoader(reader):                     # RGB tensor normalized to 0 ~ 1.
        fgr, pha, *rec = model(src.cuda(), *rec, downsample_ratio)  # Cycle the recurrent states.
        #pha = pha * 4
        #pha[pha > 0.3] = 1
        com = fgr * pha + bgr * (1 - pha)              # Composite to green background. 
        writer.write(com)                              # Write frame.

# Load the model.
#model = torch.hub.load("PeterL1n/RobustVideoMatting", "resnet50") # or "resnet50"

# Converter API.
#convert_video = torch.hub.load("PeterL1n/RobustVideoMatting", "converter")
'''