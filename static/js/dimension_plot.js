// Model name mapping
import { 
    modelNameMapping, 
    inputFormatMapping, 
    outputFormatMapping, 
    appMapping, 
    skillsMapping,
    modelOrder,
    modelColorMapping
} from './mapping.js';


const modelSets = {
    all: modelOrder,
    all_flagship: ['GPT-4o (0513)', 'Claude-3.5-Sonnet (0620)', 'Claude-3.5-Sonnet (1022)', 'Gemini-1.5-Pro-002', 'Qwen2-VL-72B', 'InternVL2-Llama3-76B', 'LLaVA-OneVision-72B'],
    all_efficiency: ['Gemini-1.5-Flash-002', 'GPT-4O Mini', 'Qwen2-VL-7B', 'Pixtral 12B', 'InternVL2-8B', 'Phi-3.5-Vision', 'MiniCPM-V2.6', 'LLaVA-OneVision-7B', 'Llama-3.2-11B', 'Idefics3-8B-Llama3', 'Mammoth-VL-8B'],
    prop_flagship: ['GPT-4o (0513)', 'Claude-3.5-Sonnet (0620)', 'Claude-3.5-Sonnet (1022)', 'Gemini-1.5-Pro-002'],
    open_source_efficiency: ['Qwen2-VL-7B', 'Pixtral 12B', 'InternVL2-8B', 'Phi-3.5-Vision', 'MiniCPM-V2.6', 'LLaVA-OneVision-7B', 'Llama-3.2-11B', 'Idefics3-8B-Llama3', 'Mammoth-VL-8B'],
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


        // Plot the default radar chart (for "skills" and "all" models)
        updateChart();
    });



function getShortLabel(dimension, longLabel) {
    switch(dimension) {
        case 'input_format':
            return inputFormatMapping[longLabel] || longLabel;
        case 'output_format':
            return outputFormatMapping[longLabel] || longLabel;
        case 'app':
            return appMapping[longLabel] || longLabel;
        case 'skills':
            return skillsMapping[longLabel] || longLabel;
        default:
            return longLabel;
    }
}

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

    // Use getShortLabel when setting labels
    radarData.labels = Array.from(dimensionSet).sort().map(label => getShortLabel(dimensionKey, label));

    // Find the maximum value across all models and fields
    let maxValue = 0;
    modelOrder.forEach(modelName => {
        const dataModelName = modelNameMapping[modelName];
        const modelData = data[dataModelName]?.[dimensionKey] || {};
        radarData.labels.forEach(shortLabel => {
            const longLabel = Object.keys(modelData).find(key => getShortLabel(dimensionKey, key) === shortLabel);
            const value = modelData[longLabel]?.average_score || 0;
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

        radarData.labels.forEach(shortLabel => {
            const longLabel = Object.keys(modelData).find(key => getShortLabel(dimensionKey, key) === shortLabel);
            const fieldData = modelData[longLabel];
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
                    beginAtZero: false,
                    ticks: {
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
