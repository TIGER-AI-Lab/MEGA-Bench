// Model name mapping
import { 
    modelNameMapping, 
    inputFormatMapping, 
    outputFormatMapping, 
    appMapping, 
    skillsMapping,
    modelOrder,
    modelColorMapping,
    dimensionTitleMapping
} from './mapping.js';



// Dimensions for the radar charts
const dimensions = ['skills', 'input_format', 'output_format', 'input_num', 'app'];

let globalData;
let chartInstances = [];

// Fetch and load JSON data
fetch('./static/data/all_model_keywords_stats.json')
    .then(response => response.json())
    .then(data => {
        globalData = data;
        
        // Populate model select options
        const modelSelect1 = document.getElementById('model-select-1');
        const modelSelect2 = document.getElementById('model-select-2');
        
        modelOrder.forEach(modelName => {
            const option1 = document.createElement('option');
            option1.value = modelName;
            option1.textContent = modelName;
            modelSelect1.appendChild(option1);

            const option2 = document.createElement('option');
            option2.value = modelName;
            option2.textContent = modelName;
            modelSelect2.appendChild(option2);
        });

        // Add event listeners for model selection changes
        modelSelect1.addEventListener('change', updateCharts);
        modelSelect2.addEventListener('change', updateCharts);

        // Update the "Back to Main Chart" button href
        const backButton = document.querySelector('a.button.is-link');
        if (backButton) {
            backButton.href = 'index.html#radar-charts';
        }

        // Initial chart creation
        updateCharts();
    });

function updateCharts() {
    const selectedModel1 = document.getElementById('model-select-1').value;
    const selectedModel2 = document.getElementById('model-select-2').value;
    const containerElement = document.getElementById('radar-charts-container');
    
    // Clear existing charts
    containerElement.innerHTML = '';
    chartInstances.forEach(chart => chart.destroy());
    chartInstances = [];

    // Create a chart for each dimension
    dimensions.forEach(dimension => {
        const chartContainer = document.createElement('div');
        chartContainer.className = 'chart-container';
        
        const canvas = document.createElement('canvas');
        chartContainer.appendChild(canvas);
        containerElement.appendChild(chartContainer);

        const radarData = prepareRadarData(globalData, selectedModel1, selectedModel2, dimension);
        const chart = createRadarChart(canvas, radarData, dimension);
        chartInstances.push(chart);
    });
}

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

function prepareRadarData(data, modelName1, modelName2, dimensionKey) {
    const radarData = {
        labels: [],
        datasets: []
    };

    const dataModelName1 = modelNameMapping[modelName1];
    const modelData1 = data[dataModelName1]?.[dimensionKey] || {};

    // Use getShortLabel when setting labels
    radarData.labels = Object.keys(modelData1).sort().map(label => getShortLabel(dimensionKey, label));

    // Normalize the data to 0-1 range if necessary
    const maxValue1 = Math.max(...Object.values(modelData1).map(field => field?.average_score || 0));
    const normalizeValue = (value, maxValue) => maxValue > 1 ? value / maxValue : value;

    const dataset1 = {
        label: modelName1,
        data: radarData.labels.map(shortLabel => {
            const longLabel = Object.keys(modelData1).find(key => getShortLabel(dimensionKey, key) === shortLabel);
            return normalizeValue(modelData1[longLabel]?.average_score || 0, maxValue1);
        }),
        fill: true,
        borderColor: modelColorMapping[modelName1],
        backgroundColor: modelColorMapping[modelName1].replace('0.6', '0.2')
    };

    radarData.datasets.push(dataset1);

    if (modelName2 && modelName2 !== "") {
        const dataModelName2 = modelNameMapping[modelName2];
        const modelData2 = data[dataModelName2]?.[dimensionKey] || {};
        const maxValue2 = Math.max(...Object.values(modelData2).map(field => field?.average_score || 0));

        const dataset2 = {
            label: modelName2,
            data: radarData.labels.map(shortLabel => {
                const longLabel = Object.keys(modelData2).find(key => getShortLabel(dimensionKey, key) === shortLabel);
                return normalizeValue(modelData2[longLabel]?.average_score || 0, maxValue2);
            }),
            fill: true,
            borderColor: modelColorMapping[modelName2],
            backgroundColor: modelColorMapping[modelName2].replace('0.6', '0.2')
        };

        radarData.datasets.push(dataset2);
    }

    return radarData;
}

function createRadarChart(canvas, radarData, dimension) {
    return new Chart(canvas.getContext('2d'), {
        type: 'radar',
        data: radarData,
        options: {
            responsive: true,
            maintainAspectRatio: false,
            scales: {
                r: {
                    beginAtZero: true,
                    min: 0,
                    max: 1,
                    ticks: {
                        stepSize: 0.2,
                        font: {
                            size: 12
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
                    display: true,
                    position: 'top',
                    labels: {
                        font: {
                            size: 14
                        },
                        padding: 20
                    }
                },
                title: {
                    display: true,
                    text: dimensionTitleMapping[dimension] || dimension.charAt(0).toUpperCase() + dimension.slice(1).replace('_', ' '),
                    font: {
                        size: 20,
                        weight: 'bold'
                    },
                    padding: {
                        top: 10,
                        bottom: 30
                    }
                },
                tooltip: {
                    bodyFont: {
                        size: 14
                    },
                    titleFont: {
                        size: 16
                    }
                }
            },
            elements: {
                point: {
                    radius: 4,
                    hoverRadius: 6
                },
                line: {
                    borderWidth: 3
                }
            }
        }
    });
}
