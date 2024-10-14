// Model name mapping
const modelNameMapping = {
    'GPT-4o (0513)': 'GPT_4o',
    'Claude-3.5-Sonnet': 'Claude_3.5',
    'Gemini-1.5-Pro-002': 'Gemini_1.5_pro_002',
    'Gemini-1.5-Flash-002': 'Gemini_1.5_flash_002',
    'GPT-4O Mini': 'GPT_4o_mini',
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
};

// Dimensions for the radar chart
const dimensions = ['skills', 'input_format', 'output_format', 'input_num', 'app'];

// Model order (desired display order)
const modelOrder = [
    'GPT-4o (0513)',
    'Claude-3.5-Sonnet',
    'Gemini-1.5-Pro-002',
    'Gemini-1.5-Flash-002',
    'GPT-4O Mini',
    'Qwen2-VL-72B',
    'InternVL2-Llama3-76B',
    'LLaVA-OneVision-72B',
    'Qwen2-VL-7B',
    'Pixtral 12B',
    'InternVL2-8B',
    'Phi-3.5-Vision',
    'MiniCPM-V2.6',
    'LLaVA-OneVision-7B',
    'Llama-3.2-11B',
    'Idefics3-8B-Llama3',
];

// Define a consistent color mapping for models
const modelColorMapping = {
    'GPT-4o (0513)': 'rgba(255, 99, 132, 0.6)',
    'Claude-3.5-Sonnet': 'rgba(54, 162, 235, 0.6)', 
    'Gemini-1.5-Pro-002': 'rgba(75, 192, 192, 0.6)',
    'Gemini-1.5-Flash-002': 'rgba(153, 102, 255, 0.6)', 
    'GPT-4O Mini': 'rgba(255, 159, 64, 0.6)',
    'Qwen2-VL-72B': 'rgba(255, 205, 86, 0.6)', 
    'InternVL2-Llama3-76B': 'rgba(201, 203, 207, 0.6)', 
    'LLaVA-OneVision-72B': 'rgba(140, 82, 255, 0.6)', 
    'Qwen2-VL-7B': 'rgba(255, 87, 51, 0.6)', 
    'Pixtral 12B': 'rgba(220, 220, 220, 0.6)', 
    'InternVL2-8B': 'rgba(52, 152, 219, 0.6)', 
    'Phi-3.5-Vision': 'rgba(46, 204, 113, 0.6)', 
    'MiniCPM-V2.6': 'rgba(230, 126, 34, 0.6)', 
    'LLaVA-OneVision-7B': 'rgba(231, 76, 60, 0.6)', 
    'Llama-3.2-11B': 'rgba(52, 73, 94, 0.6)', 
    'Idefics3-8B-Llama3': 'rgba(241, 196, 15, 0.6)',
};

// List of models visible by default
const defaultVisibleModels = ['GPT-4o (0513)', 'Claude-3.5-Sonnet', 'Gemini-1.5-Pro-002'];

const modelSets = {
    all: modelOrder,
    all_flagship: ['GPT-4o (0513)', 'Claude-3.5-Sonnet', 'Gemini-1.5-Pro-002', 'Qwen2-VL-72B', 'InternVL2-Llama3-76B', 'LLaVA-OneVision-72B'],
    all_efficiency: ['Gemini-1.5-Flash-002', 'GPT-4O Mini', 'Qwen2-VL-7B', 'Pixtral 12B', 'InternVL2-8B', 'Phi-3.5-Vision', 'MiniCPM-V2.6', 'LLaVA-OneVision-7B', 'Llama-3.2-11B', 'Idefics3-8B-Llama3'],
    prop_flagship: ['GPT-4o (0513)', 'Claude-3.5-Sonnet', 'Gemini-1.5-Pro-002'],
    open_source_efficiency: ['Qwen2-VL-7B', 'Pixtral 12B', 'InternVL2-8B', 'Phi-3.5-Vision', 'MiniCPM-V2.6', 'LLaVA-OneVision-7B', 'Llama-3.2-11B', 'Idefics3-8B-Llama3'],
    open_source_flagship: ['Qwen2-VL-72B', 'InternVL2-Llama3-76B', 'LLaVA-OneVision-72B'],
    prop_efficiency: ['Gemini-1.5-Flash-002', 'GPT-4O Mini']
};


let radarChartInstance; // To store the chart instance for updating
let globalData

// Fetch and load JSON data
fetch('./static/data/all_model_keywords_stats.json')
    .then(response => response.json())
    .then(data => {
        globalData = data; // Store the data globally
        
        // Add event listeners for dropdown selection changes
        document.getElementById('dimension-select').addEventListener('change', updateChart);
        document.getElementById('model-set-select').addEventListener('change', updateChart);

        // Populate dimension select options
        const dimensionSelect = document.getElementById('dimension-select');
        dimensions.forEach(dimension => {
            const option = document.createElement('option');
            option.value = dimension;
            option.textContent = dimension.replace('_', ' ').charAt(0).toUpperCase() + dimension.slice(1);
            dimensionSelect.appendChild(option);
        });

        // Populate model set select options
        const modelSetSelect = document.getElementById('model-set-select');
        Object.keys(modelSets).forEach(setName => {
            const option = document.createElement('option');
            option.value = setName;
            option.textContent = setName.replace('_', ' ').charAt(0).toUpperCase() + setName.slice(1);
            modelSetSelect.appendChild(option);
        });

        // Plot the default radar chart (for "skills" and "all" models)
        updateChart();
    });

// Function to update the chart based on current selections
function updateChart() {
    const selectedDimension = document.getElementById('dimension-select').value;
    const selectedModelSet = document.getElementById('model-set-select').value;
    const visibleModels = modelSets[selectedModelSet];
    
    const radarData = prepareRadarData(globalData, selectedDimension, visibleModels);
    updateRadarChart(radarData, selectedDimension);
}


function prepareRadarData(data, dimensionKey, visibleModels) {
    const radarData = {
        labels: [],
        datasets: []
    };

    const dimensionSet = new Set();
    Object.keys(data).forEach(model => {
        const dimensionData = data[model]?.[dimensionKey] || {};
        Object.keys(dimensionData).forEach(field => dimensionSet.add(field));
    });

    radarData.labels = Array.from(dimensionSet).sort();

    // Find the maximum value across all models and fields
    let maxValue = 0;
    modelOrder.forEach(modelName => {
        const dataModelName = modelNameMapping[modelName];
        const modelData = data[dataModelName]?.[dimensionKey] || {};
        radarData.labels.forEach(field => {
            const value = modelData[field]?.average_score || 0;
            maxValue = Math.max(maxValue, value);
        });
    });

    // Normalize function
    const normalize = (value) => maxValue > 1 ? value / maxValue : value;

    modelOrder.forEach(modelName => {
        const dataset = {
            label: modelName,
            data: [],
            fill: true,
            borderColor: modelColorMapping[modelName],
            backgroundColor: modelColorMapping[modelName].replace('0.6', '0.2'),
            hidden: !visibleModels.includes(modelName)
        };

        const dataModelName = modelNameMapping[modelName];
        const modelData = data[dataModelName]?.[dimensionKey] || {};

        radarData.labels.forEach(field => {
            const fieldData = modelData[field];
            dataset.data.push(normalize(fieldData?.average_score || 0));
        });

        radarData.datasets.push(dataset);
    });

    return radarData;
}


function createRadarChart(radarData, dimension) {
    const ctx = document.getElementById('radarChart').getContext('2d');
    radarChartInstance = new Chart(ctx, {
        type: 'radar',
        data: radarData,
        options: {
            responsive: true,
            scales: {
                r: {
                    beginAtZero: true,
                    min: 0,
                    max: 1,
                    ticks: {
                        stepSize: 0.2,
                        font: {
                            size: 16
                        }
                    },
                    pointLabels: {
                        font: {
                            size: 14
                        },
                        callback: function(label) {
                            const words = label.split(' ');
                            const lines = [];
                            let currentLine = '';

                            words.forEach(word => {
                                if (currentLine.length + word.length <= 15) {
                                    currentLine += (currentLine ? ' ' : '') + word;
                                } else {
                                    lines.push(currentLine);
                                    currentLine = word;
                                }
                            });
                            if (currentLine) {
                                lines.push(currentLine);
                            }
                            return lines;
                        }
                    }
                }
            },
            plugins: {
                legend: {
                    labels: {
                        font: {
                            size: 14
                        }
                    },
                    onClick: function (e, legendItem) {
                        const index = legendItem.datasetIndex;
                        const chart = this.chart;
                        const meta = chart.getDatasetMeta(index);
                        meta.hidden = meta.hidden === null ? !chart.data.datasets[index].hidden : null;
                        chart.update();
                    }
                }
            }
        }
    });
}


// Modified updateRadarChart function
function updateRadarChart(radarData, dimension) {
    if (radarChartInstance) {
        radarChartInstance.destroy();
    }
    createRadarChart(radarData, dimension);
}