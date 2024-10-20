// Function to load CSV data from a file
function loadCSVData(url) {
    return fetch(url)
    .then(response => {
        if (!response.ok) {
        throw new Error(`Could not fetch the CSV file at ${url}`);
        }
        return response.text();
    })
    .then(csvText => parseCSV(csvText))
    .catch(error => console.error(error));
  }
  
// Function to parse CSV data
function parseCSV(csv) {
    var lines = csv.trim().split('\n');
    var headers = lines[0].split(',');
    var data = [];

    for (var i = 1; i < lines.length; i++) {
        var obj = {};
        var currentline = lines[i].split(',');

        for (var j = 0; j < headers.length; j++) {
            obj[headers[j].trim()] = currentline[j] ? currentline[j].trim() : "";
        }

        data.push(obj);
    }

    console.log("Parsed CSV data:", data);
    return data;
}


var customColors = [
    0x41bfc8,
    0x16a6df,
    0x1b5883,
    0x9823d7,
    0xe52ea2,
    0xd80e0e,
    0xf48506,
    0xC95C49,
];

var categoryOrder = [
    "Information Extraction",
    "Planning",
    "Coding",
    "Perception",
    "Metrics",
    "Science",
    "Knowledge",
    "Mathematics",
];


var series
var hierarchicalData
var originalData


function buildHierarchy(data) {
    var rootNode = { name: "MEGA-BENCH", children: [] };
    var categoryColorMap = new Map();

    // Create a map of categories to colors
    categoryOrder.forEach((category, index) => {
        categoryColorMap.set(category, customColors[index]);
    });

    function formatColor(color) {
        if (typeof color === 'string' && color.startsWith('#')) {
            return color;
        }

        if (typeof color === 'number') {
            return '#' + color.toString(16).padStart(6, '0');
        }

        if (typeof color === 'string') {
            return '#' + color;
        }
        console.warn("Invalid color format:", color);
        return '#CCCCCC'; 
    }

    function lightenColor(color, percent) {
        color = formatColor(color).replace('#', '');
        var num = parseInt(color, 16),
            amt = Math.round(2.55 * percent),
            R = (num >> 16) + amt,
            G = (num >> 8 & 0x00FF) + amt,
            B = (num & 0x0000FF) + amt;
        return '#' + ((0x1000000 + (R<255?R<1?0:R:255)*0x10000 + (G<255?G<1?0:G:255)*0x100 + (B<255?B<1?0:B:255)).toString(16).slice(1));
    }

    // New function to make colors significantly lighter
    function makeMuchLighter(color) {
        return lightenColor(color, 40); // Increase this value to make colors even lighter
    }

    data.forEach(function(item) {
        var levels = ['Level 1', 'Level 2', 'Level 3', 'Level 4', 'Level 5'];
        var currentNode = rootNode;
        var baseColor;

        for (let i = 0; i < levels.length; i++) {
            var levelName = item[levels[i]];
            if (!levelName) break;  // Stop if we reach an undefined level

            var childNode = currentNode.children.find(node => node.name === levelName);
            if (!childNode) {
                if (i === 0) {
                    baseColor = formatColor(categoryColorMap.get(levelName) || customColors[categoryColorMap.size % customColors.length]);
                    baseColor = makeMuchLighter(baseColor); // Make first level color much lighter
                }
                childNode = { 
                    name: levelName, 
                    originalName: levelName.replace(/\s+/g, '_'), // Store original name
                    children: [],
                    color: i === 0 ? baseColor : lightenColor(baseColor, (i) * 8)
                };
                currentNode.children.push(childNode);
            } else {
                // If the node already exists, ensure it uses the correct base color
                baseColor = baseColor || childNode.color;
            }
            currentNode = childNode;
        }

        // Add value to the deepest level
        if (currentNode !== rootNode) {
            if (!currentNode.value) currentNode.value = 0;
            currentNode.value += 1;
        }
    });

    // Sort the top-level children based on the categoryOrder
    rootNode.children.sort((a, b) => {
        return categoryOrder.indexOf(a.name) - categoryOrder.indexOf(b.name);
    });

    hierarchicalData = rootNode

    return rootNode;
}


function setUpFont() {
    series.labels.template.adapters.add("text", function(text, target) {
        if (target.dataItem) {
            var label = target.dataItem.get("category");
            return customBreakWords(label, 10);
        }
        return text;
    });

    series.labels.template.adapters.add("fontSize", function(fontSize, target) {
        if (target.dataItem && target.dataItem.get("depth") === 1) {
            return 14;
        }
        return fontSize;
    });
}

function getSeriesCenter(series) {
    var container = series.root.container;
    var centerX = container.width() / 2;
    var centerY = container.height() / 2;
    return { x: centerX, y: centerY };
}




function createChart(hierarchicalData) {
    var root = am5.Root.new("chartdiv");
    root.setThemes([am5themes_Animated.new(root)]);

    series = root.container.children.push(
        am5hierarchy.Sunburst.new(root, {
            downDepth: 3,
            initialDepth: 5,
            valueField: "value",
            categoryField: "name",
            childDataField: "children",
            innerRadius: am5.percent(15),
        })
    );

    series.slices.template.setAll({
        strokeWidth: 1,
        stroke: am5.color(0xffffff),
        toggleKey: "none",
        clickTarget: "self",
        cursorOverStyle: "pointer",
        interactive: true 
    });

    series.slices.template.states.create("hover", {
        scale: 1.05
    });

    series.labels.template.setAll({
        text: "{category}",
        fill: am5.color(0x000000),
        strokeWidth: 0,
        fontFamily: "Roboto, sans-serif", // Use the vector font here
        fontSize: 12,
        // maxWidth: 120,
        crisp: true
    });


    // Add this new adapter for label rotation
    series.labels.template.adapters.add("rotation", function(rotation, target) {
        if (target.dataItem && target.dataItem.get("depth") === 1) {
            var name = target.dataItem.get("category");
            if (name === "Perception" || name === "Planning") {
                return 0; // Set rotation to 0 for horizontal text
            }
        }
        return rotation; // Default rotation for other labels
    });

    // Add this new adapter for label text alignment
    series.labels.template.adapters.add("textAlign", function(align, target) {
        if (target.dataItem && target.dataItem.get("depth") === 1) {
            var name = target.dataItem.get("category");
            if (name === "Perception" || name === "Planning") {
                return "center"; // Center align the text
            }
        }
        return align; // Default alignment for other labels
    });

    setUpFont();

    series.slices.template.adapters.add("fill", function(fill, target) {
        var dataItem = target.dataItem;
        if (dataItem) {
            if (dataItem.get("depth") === 0) {
                return am5.color(0xFFFFFF); 
            }
            return am5.color(dataItem.dataContext.color || 0xCCCCCC);
        }
        return am5.color(0xCCCCCC);
    });

    series.labels.template.adapters.add("forceHidden", function(forceHidden, target) {
        return target.dataItem && target.dataItem.get("depth") === 0;
    });

    originalData = JSON.parse(JSON.stringify(hierarchicalData));


    setUpCenter(root);

    setupLeafNodeClick(series)

    series.data.setAll([hierarchicalData]);

    series.appear(2000, 100);

}

function setupLeafNodeClick(series) {
    series.slices.template.events.on("click", function(ev) {
        var dataItem = ev.target.dataItem;
        if (dataItem && dataItem.get("children").length === 0) {
            // This is a leaf node
            var path = buildPath(dataItem);
            var url = `https://github.com/TIGER-AI-Lab/MEGA-Bench-task-examples/tree/main/task_examples/${path}`;
            window.open(url, "_blank");
        }
    });

    // Change cursor to pointer for leaf nodes
    series.slices.template.adapters.add("cursorOverStyle", function(cursorOverStyle, target) {
        var dataItem = target.dataItem;
        if (dataItem && dataItem.get("children").length === 0) {
            return "pointer";
        }
        return cursorOverStyle;
    });
}

function buildPath(dataItem) {
    var path = [];
    var currentItem = dataItem;
    
    while (currentItem && currentItem.get("depth") > 0) {
        path.unshift(currentItem.dataContext.originalName || currentItem.get("category"));
        currentItem = currentItem.get("parent");
    }
    
    return path.join('/');
}


function customBreakWords(text, maxLength) {
    if (text.length <= maxLength) return text;
    var parts = text.split(/\s+/);
    var lines = [];
    var currentLine = "";
    
    for (var i = 0; i < parts.length; i++) {
        var word = parts[i];
        if ((currentLine + word).length > maxLength) {
            if (currentLine) lines.push(currentLine);
            currentLine = word;
        } else {
            currentLine += (currentLine ? " " : "") + word;
        }
    }
    if (currentLine) lines.push(currentLine);
    return lines.join("\n");
}

function setUpCenter(root) {
    var centerContainer = root.container.children.push(am5.Container.new(root, {
        width: 140,
        height: 140,
        zIndex: 1000
    }));
    
    var logo = centerContainer.children.push(am5.Picture.new(root, {
        width: 110,
        height: 110,
        centerX: am5.p50,
        centerY: am5.p50,
        src: "static/images/mega-bench-logo_no_shadow.png",
    }));


    logo.events.on("click", function() {
        console.log("Logo clicked");

        if (root) {
            console.log("Disposing of the chart");

            // Dispose of the existing chart
            root.dispose();

            // Recreate the chart with the original data
            createChart(hierarchicalData);

            console.log("Chart recreated");
        } else {
            console.error("Root is not defined");
        }
    });
    

    function updatePosition() {
        var center = getSeriesCenter(series);
        centerContainer.setAll({
            x: center.x,  
            y: center.y   
        });
    }

    updatePosition();

    series.root.container.events.on("sizechanged", updatePosition);

    return centerContainer;
}



loadCSVData('./static/data/taxonomy_new.csv').then(function(csvParsedData) {

    console.log(csvParsedData)

    buildHierarchy(csvParsedData);
    createChart(hierarchicalData);
});

