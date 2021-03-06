from fvcore.common.config import CfgNode
from Archs_2D import Register

CONFIGS = CfgNode()
CONFIGS.INTENSOR_SHAPE = (288, 288)
CONFIGS.BATCH_SIZE = 32
CONFIGS.DEVICE = 'cuda'

CONFIGS.TRAINING = CfgNode()
CONFIGS.TRAINING.LOGDIR = './logdirs/mobiv2_retinanet'
CONFIGS.TRAINING.CHECKPOINT_MODE = 'RESUME'#['PRETRAINED', 'RESUME', 'START']
CONFIGS.TRAINING.CHECKPOINT_FILE = './pretrained/mobilenetv2_pretrained.pkl'

CONFIGS.DATASET = CfgNode()
CONFIGS.DATASET.PATH = './datasets/data/kitti'
CONFIGS.DATASET.MEAN = [95.87739305, 98.76049672, 93.83309082]

CONFIGS.DATALOADER = CfgNode()
CONFIGS.DATALOADER.SAMPLER_TRAIN = 'TrainingSampler'
# Solver
# ---------------------------------------------------------------------------- #
CONFIGS.SOLVER = CfgNode()

# See detectron2/solver/build.py for LR scheduler options
CONFIGS.SOLVER.LR_SCHEDULER_NAME = "WarmupMultiStepLR"

CONFIGS.SOLVER.MAX_ITER = 400000

CONFIGS.SOLVER.BASE_LR = 0.01 

CONFIGS.SOLVER.MOMENTUM = 0.9

CONFIGS.SOLVER.WEIGHT_DECAY = 0.0001
# The weight decay that's applied to parameters of normalization layers
# (typically the affine transformation)
CONFIGS.SOLVER.WEIGHT_DECAY_NORM = 0.0

CONFIGS.SOLVER.GAMMA = 0.1
# The iteration number to decrease learning rate by GAMMA.
CONFIGS.SOLVER.STEPS = (50000, 80000)

CONFIGS.SOLVER.WARMUP_FACTOR = 1.0 / 1000
CONFIGS.SOLVER.WARMUP_ITERS = 1000
CONFIGS.SOLVER.WARMUP_METHOD = "linear"


# Detectron v1 (and previous detection code) used a 2x higher LR and 0 WD for
# biases. This is not useful (at least for recent models). You should avoid
# changing these and they exist only to reproduce Detectron v1 training if
# desired.
CONFIGS.SOLVER.BIAS_LR_FACTOR = 1.0
CONFIGS.SOLVER.WEIGHT_DECAY_BIAS = CONFIGS.SOLVER.WEIGHT_DECAY

CONFIGS.MOBILENETV2 = CfgNode()

CONFIGS.EXTRANET = CfgNode()
CONFIGS.EXTRANET.NUMLAYERS = 2
CONFIGS.EXTRANET.NUMCONVS = 1
CONFIGS.EXTRANET.USE_INV_RES = False
CONFIGS.EXTRANET.EXPAND_RATIO = 1

CONFIGS.RETINANET = CfgNode()
CONFIGS.RETINANET.NUM_CLASSES = 8
CONFIGS.RETINANET.OUT_CHANNELS = 256
CONFIGS.RETINANET.PRIOR_PROB = 0.01
CONFIGS.RETINANET.HEADER_NUMCONVS = 2
CONFIGS.RETINANET.IOU_THRESHOLDS = [0.4, 0.5]
CONFIGS.RETINANET.IOU_LABELS = [0, -1, 1]
CONFIGS.RETINANET.OD_FEATURES = ['fpn_layer0', 'fpn_layer1', 'fpn_layer2', 'extra_layer1', 'extra_layer2']
CONFIGS.RETINANET.FOCAL_LOSS_GAMMA = 2.0
CONFIGS.RETINANET.FOCAL_LOSS_ALPHA = 0.25
CONFIGS.RETINANET.SMOOTH_L1_LOSS_BETA = 0.1

CONFIGS.RPN = CfgNode()
CONFIGS.RPN.BBOX_REG_WEIGHTS = (1.0, 1.0, 1.0, 1.0)

CONFIGS.ANCHOR_GENERATOR = CfgNode()
CONFIGS.ANCHOR_GENERATOR.SIZES = [[x, x * 2**(1.0/3), x * 2**(2.0/3)] for x in [10, 20, 40, 80, 160]]
CONFIGS.ANCHOR_GENERATOR.ASPECT_RATIOS = [[0.5, 1.0, 2.0]]
CONFIGS.ANCHOR_GENERATOR.OFFSET = 0.0

CONFIGS.FPN = CfgNode()
CONFIGS.FPN.IN_FEATURES = ['mobilev2_layer6', 'mobilev2_layer13', 'mobilev2_layer18']
CONFIGS.FPN.FUSE_TYPE = 'sum' #['avg', 'sum']
CONFIGS.FPN.UPSAMPLE_TYPE = 'nearest' #['nearest', 'linear', 'bilinear', 'bicubic' and 'trilinear']
CONFIGS.FPN.USE_INV_RES = False

CONFIGS.DETECTOR = CfgNode()
CONFIGS.DETECTOR.CHECKPOINT = './logdirs/mobiv2_retinanet/retinanet_mobilev2_386000.pkl'
CONFIGS.DETECTOR.SCORE_THRESH_TEST = 0.5
CONFIGS.DETECTOR.TOPK_CANDIDATES_TEST = 1000
CONFIGS.DETECTOR.NMS_THRESH_TEST = 0.5
CONFIGS.DETECTOR.DETECTIONS_PER_IMAGE = 100

CONFIGS.INPUT = CfgNode()
CONFIGS.INPUT.FORMAT = 'BGR'

@Register.Config.register('MOBI-V2-RETINA-FPN')
def register():
    return CONFIGS


