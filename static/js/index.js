$(document).ready(function() {
  const options = {
    slidesToScroll: 1,
    slidesToShow: 1,
    loop: true,
    infinite: true,
    autoplay: false,
    autoplaySpeed: 3000,
  }
  // Initialize all div with carousel class
  const carousels = bulmaCarousel.attach('.carousel', options);

})

document.addEventListener('DOMContentLoaded', function() {
  loadTableData();
  window.addEventListener('resize', adjustNameColumnWidth);

  const toggleButton = document.getElementById('toggleTable');
  const leaderboardContainer = document.querySelector('.leaderboard-container');
  const buttonText = toggleButton.querySelector('span:not(.icon)');
  const buttonIcon = toggleButton.querySelector('.fas');

  toggleButton.addEventListener('click', function() {
    const isHidden = leaderboardContainer.style.display === 'none';
    
    // Toggle the table visibility
    leaderboardContainer.style.display = isHidden ? 'block' : 'none';
    
    // Update button text and icon
    buttonText.textContent = isHidden ? 'Hide Leaderboard Summary' : 'Show Leaderboard Summary';
    buttonIcon.classList.toggle('fa-chevron-up');
    buttonIcon.classList.toggle('fa-chevron-down');
  });
});

var mapping = {
  'GPT_4o': 'GPT-4o (0513)',
  'Claude_3.5': 'Claude-3.5-Sonnet',
  'Gemini_1.5_pro_002': 'Gemini-1.5-Pro-002',
  'Gemini_1.5_flash_002': 'Gemini-1.5-Flash-002',
  'GPT_4o_mini': 'GPT-4O Mini',
  'Qwen2_VL_72B': 'Qwen2-VL-72B',
  'InternVL2_76B': 'InternVL2-Llama3-76B',
  'llava_onevision_72B': 'LLaVA-OneVision-72B',
  'Qwen2_VL_7B': 'Qwen2-VL-7B',
  'Pixtral_12B': 'Pixtral 12B',
  'InternVL2_8B': 'InternVL2-8B',
  'Phi-3.5-vision': 'Phi-3.5-Vision',
  'MiniCPM_v2.6': 'MiniCPM-V2.6',
  'llava_onevision_7B': 'LLaVA-OneVision-7B',
  'Llama_3_2_11B': 'Llama-3.2-11B',
  'Idefics3': 'Idefics3-8B-Llama3'
};

const proprietaryModels = new Set([
  'GPT-4o (0513)', 'Claude-3.5-Sonnet', 'Gemini-1.5-Pro-002', 'Gemini-1.5-Flash-002', 'GPT-4O Mini'
]);

function loadTableData() {
  fetch('./static/data/all_summary.json')
    .then(response => {
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
      return response.json();
    })
    .then(data => {
      const tbody = document.querySelector('#mmmu-table tbody');

      // Prepare data for styling
      const overallScores = prepareScoresForStyling(Object.values(data).map(model => model.overall_score));
      const coreScores = prepareScoresForStyling(Object.values(data).map(model => 
        Math.max(model.core_noncot.macro_mean_score, model.core_cot.macro_mean_score)
      ));
      const openScores = prepareScoresForStyling(Object.values(data).map(model => model.open.macro_mean_score));

      Object.entries(data).forEach(([modelKey, modelData], index) => {
        const modelName = mapping[modelKey] || modelKey;
        const tr = document.createElement('tr');
        tr.classList.add(getModelTypeClass(modelName));
        
        const coreScore = Math.max(modelData.core_noncot.macro_mean_score, modelData.core_cot.macro_mean_score).toFixed(4);
        
        tr.innerHTML = `
          <td>${modelName}</td>
          <td class="overall-score">${applyStyle(modelData.overall_score.toFixed(4), overallScores[index])}</td>
          <td class="core-score">${applyStyle(coreScore, coreScores[index])}</td>
          <td class="open-score">${applyStyle(modelData.open.macro_mean_score.toFixed(4), openScores[index])}</td>
        `;
        tbody.appendChild(tr);
      });
      
      setupEventListeners();
      adjustNameColumnWidth();
      initializeSorting();
    })
    .catch(error => {
      console.error('Error loading table data:', error);
      document.querySelector('#mmmu-table tbody').innerHTML = `
        <tr>
          <td colspan="4">Error loading data: ${error.message}</td>
        </tr>
      `;
    });
}

function toggleCoreDetails() {
  const headerRow = document.querySelector('#mmmu-table thead tr.core-details');
  const coreCell = document.querySelector('.core-details-cell');
  const mainRows = document.querySelectorAll('#mmmu-table tbody tr');
  
  const isExpanded = headerRow.classList.contains('hidden');
  
  // Toggle visibility of header row
  headerRow.classList.toggle('hidden');
  
  // Adjust main row cells
  mainRows.forEach(row => {
    const coreOverallCell = row.querySelector('.core-overall');
    const coreNonCotCell = row.querySelector('.core-noncot');
    const coreCotCell = row.querySelector('.core-cot');
    
    if (isExpanded) {
      // Expand: hide core-overall cell, show detail cells
      coreOverallCell.classList.add('hidden');
      coreNonCotCell.classList.remove('hidden');
      coreCotCell.classList.remove('hidden');
    } else {
      // Collapse: show core-overall cell, hide detail cells
      coreOverallCell.classList.remove('hidden');
      coreNonCotCell.classList.add('hidden');
      coreCotCell.classList.add('hidden');
    }
  });
  
  // Adjust colspan of core header cell
  coreCell.setAttribute('colspan', isExpanded ? '2' : '1');
  
  adjustNameColumnWidth();
}

function setupEventListeners() {
  const coreDetailsCell = document.querySelector('.core-details-cell');
  if (coreDetailsCell) {
    coreDetailsCell.addEventListener('click', toggleCoreDetails);
  }

  const headers = document.querySelectorAll('#mmmu-table thead th.sortable');
  headers.forEach(function(header) {
    header.addEventListener('click', function() {
      sortTable(this);
    });
  });
}


function getModelTypeClass(modelName) {
  return proprietaryModels.has(modelName) ? 'proprietary' : 'open_source';
}


function sortTable(header, forceDescending = false) {
  var table = document.getElementById('mmmu-table');
  var tbody = table.querySelector('tbody');
  var rows = Array.from(tbody.querySelectorAll('tr'));
  var headers = Array.from(header.parentNode.children);
  var columnIndex = headers.indexOf(header);
  var sortType = header.dataset.sort;

  var isDescending = forceDescending || (!header.classList.contains('asc') && !header.classList.contains('desc')) || header.classList.contains('asc');

  rows.sort(function(a, b) {
    var aValue = getCellValue(a, columnIndex);
    var bValue = getCellValue(b, columnIndex);

    if (aValue === '-' && bValue !== '-') return isDescending ? 1 : -1;
    if (bValue === '-' && aValue !== '-') return isDescending ? -1 : 1;

    if (sortType === 'number') {
      return isDescending ? parseFloat(bValue) - parseFloat(aValue) : parseFloat(aValue) - parseFloat(bValue);
    } else if (sortType === 'string') {
      // For the model name column, we need to sort based on the display name
      return isDescending ? bValue.localeCompare(aValue) : aValue.localeCompare(bValue);
    }
  });

  headers.forEach(function(th) {
    th.classList.remove('asc', 'desc');
  });

  header.classList.add(isDescending ? 'desc' : 'asc');

  rows.forEach(function(row) {
    tbody.appendChild(row);
  });

  setTimeout(adjustNameColumnWidth, 0);
}

function getCellValue(row, index) {
  var cell = row.children[index];
  if (cell.classList.contains('hidden')) {
    cell = row.querySelector(`:nth-child(${index + 1}):not(.hidden)`);
  }
  return cell ? cell.textContent.trim().replace(/^[\u00A0\s]+|[\u00A0\s]+$/g, '') : '';
}



function toggleDetails(section) {
  var detailCells = document.querySelectorAll(`.${section}-details`);
  var overallCells = document.querySelectorAll(`.${section}-overall`);
  var headerCell = document.querySelector(`.${section}-details-cell`);

  detailCells.forEach(cell => cell.classList.toggle('hidden'));
  headerCell.setAttribute('colspan', headerCell.getAttribute('colspan') === '1' ? '3' : '1');

  setTimeout(adjustNameColumnWidth, 0);
}

function resetTable() {
  document.querySelectorAll('.core-noncot-details, .core-cot-details, .open-details').forEach(function(cell) {
    cell.classList.add('hidden');
  });

  document.querySelectorAll('.core-noncot-overall, .core-cot-overall, .open-overall').forEach(function(cell) {
    cell.classList.remove('hidden');
  });

  ['core-noncot', 'core-cot', 'open'].forEach(section => {
    document.querySelector(`.${section}-details-cell`).setAttribute('colspan', '1');
  });

  var overallScoreHeader = document.querySelector('#mmmu-table thead tr:last-child th.overall-score');
  sortTable(overallScoreHeader, true);

  setTimeout(adjustNameColumnWidth, 0);
}


function getCellValue(row, index) {
  var cells = Array.from(row.children);
  var cell = cells[index];

  if (cell.classList.contains('hidden')) {
    if (cell.classList.contains('pro-details') || cell.classList.contains('pro-overall')) {
      cell = cells.find(c => (c.classList.contains('pro-overall') || c.classList.contains('pro-details')) && !c.classList.contains('hidden'));
    } else if (cell.classList.contains('val-details') || cell.classList.contains('val-overall')) {
      cell = cells.find(c => (c.classList.contains('val-overall') || c.classList.contains('val-details')) && !c.classList.contains('hidden'));
    } else if (cell.classList.contains('test-details') || cell.classList.contains('test-overall')) {
      cell = cells.find(c => (c.classList.contains('test-overall') || c.classList.contains('test-details')) && !c.classList.contains('hidden'));
    }
  }
  return cell ? cell.textContent.trim() : '';
}

function initializeSorting() {
  const overallScoreHeader = document.querySelector('#mmmu-table thead th.overall-score');
  if (overallScoreHeader) {
    sortTable(overallScoreHeader, true);
  }
}

function adjustNameColumnWidth() {
  const nameColumn = document.querySelectorAll('#mmmu-table td:first-child, #mmmu-table th:first-child');
  let maxWidth = 0;

  const span = document.createElement('span');
  span.style.visibility = 'hidden';
  span.style.position = 'absolute';
  span.style.whiteSpace = 'nowrap';
  document.body.appendChild(span);

  nameColumn.forEach(cell => {
    span.textContent = cell.textContent;
    const width = span.offsetWidth;
    if (width > maxWidth) {
      maxWidth = width;
    }
  });
}

function prepareScoresForStyling(scores) {
  const sortedScores = [...new Set(scores)].sort((a, b) => b - a);
  return scores.map(score => sortedScores.indexOf(score));
}

function applyStyle(value, rank) {
  if (rank === 0) return `<b>${value}</b>`;
  if (rank === 1) return `<span style="text-decoration: underline;">${value}</span>`;
  return value;
}