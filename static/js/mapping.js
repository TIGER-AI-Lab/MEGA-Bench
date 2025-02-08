const modelNameMapping = {
    'GPT-4o (0513)': 'GPT_4o',
    'Claude-3.5-Sonnet (0620)': 'Claude_3.5',
    'Claude-3.5-Sonnet (1022)': 'Claude_3.5_new',
    'Gemini-1.5-Pro-002': 'Gemini_1.5_pro_002',
    'Gemini-1.5-Flash-002': 'Gemini_1.5_flash_002',
    'GPT-4o mini': 'GPT_4o_mini',
    'Qwen2-VL-72B': 'Qwen2_VL_72B',
    'InternVL2-Llama3-76B': 'InternVL2_76B',
    'LLaVA-OneVision-72B': 'llava_onevision_72B',
    'Qwen2-VL-7B': 'Qwen2_VL_7B',
    'Pixtral 12B': 'Pixtral_12B',
    'InternVL2-8B': 'InternVL2_8B',
    'Phi-3.5-Vision': 'Phi-3.5-vision',
    'MiniCPM-V2.6': 'MiniCPM_v2.6',
    'LLaVA-OneVision-7B': 'llava_onevision_7B',
    'Llama-3.2-11B': 'Llama_3_2_11B',
    'Idefics3-8B-Llama3': 'Idefics3',
    'MAmmoTH-VL-8B': 'Mammoth_VL',
    'Aria-MoE-25B': 'Aria',
    'NVLM-D-72B': 'NVLM',
    'Gemini-exp-1206': 'Gemini-exp-1206',
    'Gemini-Flash-2.0-exp': 'Gemini-Flash-2.0-exp',
    'Gemini-2.0-thinking': 'Gemini-2.0-thinking',
};

const inputFormatMapping = {
    'User Interface Screenshots': 'UI related',
    'Text-Based Images and Documents': 'Documents',
    'Diagrams and Data Visualizations': 'Infographics',
    'Videos': 'Videos',
    'Artistic and Creative Content': 'Arts/Creative',
    'Photographs': 'Photographs',
    '3D Models and Aerial Imagery': '3D related'
};

const outputFormatMapping = {
    'contextual_formatted_text': 'Contextual Formatted',
    'structured_output': 'Structured',
    'exact_text': 'Exact',
    'numerical_data': 'Numerical',
    'open_ended_output': 'Open-ended',
    'multiple_choice': 'Multiple-choice'
};

const appMapping = {
    'Information_Extraction': 'Info Extraction',
    'Planning': 'Planning',
    'Coding': 'Coding',
    'Perception': 'Perception',
    'Metrics': 'Metrics',
    'Science': 'Science',
    'Knowledge': 'Knowledge',
    'Mathematics': 'Math'
};

const skillsMapping = {
    'Object Recognition and Classification': 'Object Recognition',
    'Text Recognition (OCR)': 'OCR',
    'Language Understanding and Generation': 'Language Parsing/Gen',
    'Scene and Event Understanding': 'Scene Understanding',
    'Mathematical and Logical Reasoning': 'Math/Logical Reasoning',
    'Commonsense and Social Reasoning': 'Commonsense Reasoning',
    'Ethical and Safety Reasoning': 'Ethical/Safety Reasoning',
    'Domain-Specific Knowledge and Skills': 'Domain Knowledge',
    'Spatial and Temporal Reasoning': 'Spatial/Temporal Reasoning',
    'Planning and Decision Making': 'Planning/Decision Making'
};

// Model order (desired display order)
const modelOrder = [
    'GPT-4o (0513)',
    'Claude-3.5-Sonnet (1022)',
    'Claude-3.5-Sonnet (0620)',
    'Gemini-exp-1206',
    'Gemini-Flash-2.0-exp',
    'Gemini-2.0-thinking',
    'Gemini-1.5-Pro-002',
    'Gemini-1.5-Flash-002',
    'GPT-4o mini',
    'Qwen2-VL-72B',
    'InternVL2-Llama3-76B',
    'LLaVA-OneVision-72B',
    'NVLM-D-72B', 
    'Aria-MoE-25B',
    'Qwen2-VL-7B',
    'Pixtral 12B',
    'InternVL2-8B',
    'Phi-3.5-Vision',
    'Mammoth-VL-8B',
    'MiniCPM-V2.6',
    'LLaVA-OneVision-7B',
    'Llama-3.2-11B',
    'Idefics3-8B-Llama3',
];

// Color mapping for models
const modelColorMapping = {
    'GPT-4o (0513)': 'rgba(255, 99, 132, 0.6)',
    'Claude-3.5-Sonnet (0620)': 'rgba(54, 162, 235, 0.6)', 
    'Claude-3.5-Sonnet (1022)': 'rgba(75, 192, 192, 0.6)',
    'Gemini-1.5-Pro-002': 'rgba(255, 206, 86, 0.6)',
    'Gemini-1.5-Flash-002': 'rgba(75, 192, 192, 0.6)',
    'Gemini-exp-1206': 'rgba(255, 140, 0, 0.6)',
    'Gemini-Flash-2.0-exp': 'rgba(106, 90, 205, 0.6)',
    'Gemini-2.0-thinking': 'rgba(60, 179, 113, 0.6)',
    'GPT-4o mini': 'rgba(153, 102, 255, 0.6)',
    'Qwen2-VL-72B': 'rgba(255, 159, 64, 0.6)',
    'InternVL2-Llama3-76B': 'rgba(199, 199, 199, 0.6)',
    'NVLM-D-72B': 'rgba(128, 128, 0, 0.6)',
    'LLaVA-OneVision-72B': 'rgba(83, 102, 255, 0.6)',
    'Aria-MoE-25B': 'rgba(138, 43, 226, 0.6)',
    'Qwen2-VL-7B': 'rgba(255, 99, 71, 0.6)',
    'Pixtral 12B': 'rgba(50, 205, 50, 0.6)',
    'InternVL2-8B': 'rgba(255, 165, 0, 0.6)',
    'Mammoth-VL-8B': 'rgba(147, 112, 219, 0.6)',
    'Phi-3.5-Vision': 'rgba(128, 0, 128, 0.6)',
    'MiniCPM-V2.6': 'rgba(0, 128, 128, 0.6)',
    'LLaVA-OneVision-7B': 'rgba(255, 192, 203, 0.6)',
    'Llama-3.2-11B': 'rgba(165, 42, 42, 0.6)',
    'Idefics3-8B-Llama3': 'rgba(0, 255, 255, 0.6)',
};

// Add this to the existing mappings in mapping.js
const dimensionTitleMapping = {
    'skills': 'Skills',
    'input_format': 'Input Format',
    'output_format': 'Output Format',
    'input_num': 'Visual Input Number',
    'app': 'Application'
};

export { 
    modelNameMapping, 
    inputFormatMapping, 
    outputFormatMapping, 
    appMapping, 
    skillsMapping,
    modelOrder,
    modelColorMapping,
    dimensionTitleMapping
};
