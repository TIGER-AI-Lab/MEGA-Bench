import dataclasses
from enum import Enum
import functools
import os
from utils import lazy_import


@dataclasses.dataclass(frozen=True)
class ModelClassContainer:
    module_name: str
    class_name: str

    @functools.cached_property
    def impl(self):
        return lazy_import(self.module_name, self.class_name)()


class ModelClass(ModelClassContainer, Enum):
    OpenAI = ("models.OpenAI", "OpenAI")
    Claude = ("models.Claude", "Claude")
    Gemini = ("models.Gemini", "Gemini")
    Qwen2VL = ("models.Qwen2VL", "Qwen2VL")
    InternVL = ("models.InternVL", "InternVL")
    LlavaOV = ("models.LlavaOV", "LlavaOV")
    Pixtral = ("models.Pixtral", "Pixtral")
    Phi3v = ("models.Phi3v", "Phi3v")
    Grok = ("models.Grok", "Grok")
    GroundTruthOracle = ("models.GroundTruthOracle", "GroundTruthOracle")


@dataclasses.dataclass(frozen=True)
class MaxImagesPerApiCallConfig:
    max_num_image: int
    total_demo_video_frames: int


@dataclasses.dataclass(frozen=True)
class ModelTypeContainer:
    key: str
    model_name: str
    api_key: str
    constructor: type
    max_images_per_api_call: MaxImagesPerApiCallConfig = dataclasses.field(
        default=MaxImagesPerApiCallConfig(64, 8)
    )
    system_message: str | None = dataclasses.field(default=None)


class ModelType(ModelTypeContainer, Enum):

    GPT_4O_MINI = ("gpt_mini", "gpt-4o-mini", "OPENAI_API_KEY", ModelClass.OpenAI)
    GPT_4 = ("gpt-4", "gpt-4-0613", "OPENAI_API_KEY", ModelClass.OpenAI)
    GPT_4O_0513 = (
        "gpt-4o-0513",
        "gpt-4o-2024-05-13",
        "OPENAI_API_KEY",
        ModelClass.OpenAI,
    )
    GPT_4O_0806 = (
        "gpt-4o_0806",
        "gpt-4o-2024-08-06",
        "OPENAI_API_KEY",
        ModelClass.OpenAI,
    )
    CLAUDE_3_HAIKU = (
        "claude_3_haiku",
        "claude-3-haiku-20240307",
        "ANTHROPIC_API_KEY",
        ModelClass.Claude,
    )
    CLAUDE_3_5_SONNET = (
        "claude_3_5_sonnet",
        "claude-3-5-sonnet-20240620",
        "ANTHROPIC_API_KEY",
        ModelClass.Claude,
    )
    CLAUDE_3_OPUS = (
        "claude_3_opus",
        "claude-3-opus-20240229",
        "ANTHROPIC_API_KEY",
        ModelClass.Claude,
    )
    GEMINI_FLASH = (
        "gemini_flash",
        "gemini-1.5-flash-001",
        "GEMINI_API_KEY",
        ModelClass.Gemini,
        MaxImagesPerApiCallConfig(
            max_num_image=128,
            total_demo_video_frames=16,
        ),
    )
    GEMINI_FLASH_002 = (
        "gemini_flash",
        "gemini-1.5-flash-002",
        "GEMINI_API_KEY",
        ModelClass.Gemini,
        MaxImagesPerApiCallConfig(
            max_num_image=128,
            total_demo_video_frames=16,
        ),
    )
    GEMINI_PRO = (
        "gemini_pro",
        "gemini-1.5-pro-001",
        "GEMINI_API_KEY",
        ModelClass.Gemini,
    )
    GEMINI_PRO_002 = (
        "gemini_pro",
        "gemini-1.5-pro-002",
        "GEMINI_API_KEY",
        ModelClass.Gemini,
        MaxImagesPerApiCallConfig(
            max_num_image=128,
            total_demo_video_frames=16,
        ),
    )
    GEMINI_THINKING = (
        "gemini_thinking",
        "gemini-2.0-flash-thinking-exp-1219",
        "GEMINI_API_KEY",
        ModelClass.Gemini,
        MaxImagesPerApiCallConfig(
            max_num_image=100,
            total_demo_video_frames=12,
        ),
    )
    GEMINI_EXP_1206 = (
        "gemini_exp_1206",
        "gemini-exp-1206",
        "GEMINI_API_KEY",
        ModelClass.Gemini,
        MaxImagesPerApiCallConfig(
            max_num_image=128,
            total_demo_video_frames=16,
        ),
    )
    GEMINI_FLASH_2_0_EXP = (
        "gemini_flash_2.0_exp",
        "gemini-2.0-flash-exp",
        "GEMINI_API_KEY",
        ModelClass.Gemini,
        MaxImagesPerApiCallConfig(
            max_num_image=128,
            total_demo_video_frames=16,
        ),
    )
    QWEN2_VL_72B = (
        "Qwen2_VL_72B",
        "Qwen/Qwen2-VL-72B-Instruct",
        "",
        ModelClass.Qwen2VL,
        MaxImagesPerApiCallConfig(max_num_image=24, total_demo_video_frames=2),
    )
    QWEN2_VL_7B = (
        "Qwen2_VL_7B",
        "Qwen/Qwen2-VL-7B-Instruct",
        "",
        ModelClass.Qwen2VL,
        MaxImagesPerApiCallConfig(max_num_image=18, total_demo_video_frames=2),
    )
    QWEN2_VL_2B = (
        "Qwen2_VL_2B",
        "Qwen/Qwen2-VL-2B-Instruct",
        "",
        ModelClass.Qwen2VL,
        MaxImagesPerApiCallConfig(max_num_image=16, total_demo_video_frames=2),
    )
    QVQ_72B_PREVIEW = (
        "QVQ_72B_Preview",
        "Qwen/QVQ-72B-Preview",
        "",
        ModelClass.Qwen2VL,
        MaxImagesPerApiCallConfig(
            max_num_image=24,
            total_demo_video_frames=2,
        ),
    )
    INTERNVL2_LLAMA3_76B = (
        "InternVL2-Llama3-76B",
        "OpenGVLab/InternVL2-Llama3-76B",
        "",
        ModelClass.InternVL,
        MaxImagesPerApiCallConfig(max_num_image=24, total_demo_video_frames=2),
    )
    INTERNVL2_8B = (
        "InternVL2-8B",
        "OpenGVLab/InternVL2-8B",
        "",
        ModelClass.InternVL,
        MaxImagesPerApiCallConfig(max_num_image=18, total_demo_video_frames=2),
    )
    LLAVA_ONEVISION_72B = (
        "Llava_OneVision_72B",
        "lmms-lab/llava-onevision-qwen2-72b-ov-chat",
        "",
        ModelClass.LlavaOV,
        MaxImagesPerApiCallConfig(
            max_num_image=28,
            total_demo_video_frames=4,
        ),
    )
    LLAVA_ONEVISION_7B = (
        "Llava_OneVision_7B",
        "lmms-lab/llava-onevision-qwen2-7b-ov",
        "",
        ModelClass.LlavaOV,
        MaxImagesPerApiCallConfig(
            max_num_image=20,
            total_demo_video_frames=4,
        ),
    )
    PIXTRAL_12B = (
        "Pixtral-12B",
        "mistralai/Pixtral-12B-2409",
        "",
        ModelClass.Pixtral,
        MaxImagesPerApiCallConfig(
            max_num_image=48,
            total_demo_video_frames=6,
        ),
    )
    PHI_3_5_VISION = (
        "Phi_3_5_vision",
        "microsoft/Phi-3.5-vision-instruct",
        "",
        ModelClass.Phi3v,
        MaxImagesPerApiCallConfig(
            max_num_image=16,
            total_demo_video_frames=2,
        ),
    )
    # This Grok model seems to use many tokens per image.
    GROK_2_VISION_1212 = (
        "grok-2-vision",
        "grok-2-vision-1212",
        "XAI_API_KEY",
        ModelClass.Grok,
        MaxImagesPerApiCallConfig(
            max_num_image=16,
            total_demo_video_frames=2,
        ),
    )
    GROUND_TRUTH_ORACLE_SANITY_CHECK = (
        "Ground-Truth-Oracle_Sanity-Check",
        "",
        "",
        ModelClass.GroundTruthOracle,
    )

    def get_model_instance(
        self, print_response, model_path=None, **kwargs
    ):
        return self.constructor.impl(
            api_key=os.getenv(self.api_key),
            model=self.model_name if model_path is None else model_path,
            print_response=print_response,
            system_message=SYSTEM_MESSAGES.get(self),
            **dataclasses.asdict(self.max_images_per_api_call),
            **kwargs,
        )

    @staticmethod
    def from_string(s):
        try:
            return ModelType[s.upper()]
        except KeyError:
            raise ValueError(f"Invalid model type: {s}")


# Add potential system messages here
# We don't use it in our evaluation, while only relying on the task description
SYSTEM_MESSAGES = {}
