// $(document).ready(function() {
//   const options = {
//     slidesToScroll: 1,
//     slidesToShow: 1,
//     loop: true,
//     infinite: true,
//     autoplay: false,
//     autoplaySpeed: 3000,
//   }
//   // Initialize all div with carousel class
//   const carousels = bulmaCarousel.attach('.carousel', options);

// })

// document.addEventListener('DOMContentLoaded', function() {
//   loadTableData();
//   setupEventListeners();
//   window.addEventListener('resize', adjustNameColumnWidth);
// });

// function loadTableData() {
//       console.log('Starting to load table data...');
//       fetch('./leaderboard_data.json')
//         .then(response => {
//           console.log('Response status:', response.status);
//           if (!response.ok) {
//             throw new Error(`HTTP error! status: ${response.status}`);
//           }
//           return response.json();
//         })
//         .then(data => {
//           console.log('Data loaded successfully:', data);
//           const tbody = document.querySelector('#mmmu-table tbody');

//           // Prepare data for styling
//           const proScores = prepareScoresForStyling(data.leaderboardData, 'pro');
//           const valScores = prepareScoresForStyling(data.leaderboardData, 'validation');
//           const testScores = prepareScoresForStyling(data.leaderboardData, 'test');

//           data.leaderboardData.forEach((row, index) => {
//             const tr = document.createElement('tr');
//             tr.classList.add(row.info.type);
//             const nameCell = row.info.link && row.info.link.trim() !== '' ?
//               `<a href="${row.info.link}" target="_blank"><b>${row.info.name}</b></a>` :
//               `<b>${row.info.name}</b>`;
//             const safeGet = (obj, path, defaultValue = '-') => {
//               return path.split('.').reduce((acc, part) => acc && acc[part], obj) || defaultValue;
//             };

//             // Helper function to format the overall value
//             const formatOverallValue = (value, source) => {
//               // Adjust space in front of asterisk to align values
//               const adjustedValue = source === 'author' ? `&nbsp;${value || '-'}*` : `${value || '-'}`;
//               return adjustedValue;
//             };

//             const proOverall = formatOverallValue(applyStyle(safeGet(row, 'pro.overall'), proScores.overall[index]), safeGet(row, 'pro.source'));
//             const valOverall = formatOverallValue(applyStyle(safeGet(row, 'validation.overall'), valScores.overall[index]), safeGet(row, 'validation.source'));
//             const testOverall = formatOverallValue(applyStyle(safeGet(row, 'test.overall'), testScores.overall[index]), safeGet(row, 'test.source'));

//             tr.innerHTML = `
//               <td>${nameCell}</td>
//               <td>${row.info.size}</td>
//               <td>${row.info.date}</td>
//               <td class="pro-overall">${proOverall}</td>
//               <td class="hidden pro-details">${applyStyle(safeGet(row, 'pro.vision'), proScores.vision[index])}</td>
//               <td class="hidden pro-details">${applyStyle(safeGet(row, 'pro.original'), proScores.original[index])}</td>
//               <td class="val-overall">${valOverall}</td>
//               <td class="hidden val-details">${applyStyle(safeGet(row, 'validation.artDesign'), valScores.artDesign[index])}</td>
//               <td class="hidden val-details">${applyStyle(safeGet(row, 'validation.business'), valScores.business[index])}</td>
//               <td class="hidden val-details">${applyStyle(safeGet(row, 'validation.science'), valScores.science[index])}</td>
//               <td class="hidden val-details">${applyStyle(safeGet(row, 'validation.healthMedicine'), valScores.healthMedicine[index])}</td>
//               <td class="hidden val-details">${applyStyle(safeGet(row, 'validation.humanSocialSci'), valScores.humanSocialSci[index])}</td>
//               <td class="hidden val-details">${applyStyle(safeGet(row, 'validation.techEng'), valScores.techEng[index])}</td>
//               <td class="test-overall">${testOverall}</td>
//               <td class="hidden test-details">${applyStyle(safeGet(row, 'test.artDesign'), testScores.artDesign[index])}</td>
//               <td class="hidden test-details">${applyStyle(safeGet(row, 'test.business'), testScores.business[index])}</td>
//               <td class="hidden test-details">${applyStyle(safeGet(row, 'test.science'), testScores.science[index])}</td>
//               <td class="hidden test-details">${applyStyle(safeGet(row, 'test.healthMedicine'), testScores.healthMedicine[index])}</td>
//               <td class="hidden test-details">${applyStyle(safeGet(row, 'test.humanSocialSci'), testScores.humanSocialSci[index])}</td>
//               <td class="hidden test-details">${applyStyle(safeGet(row, 'test.techEng'), testScores.techEng[index])}</td>
//             `;
//             tbody.appendChild(tr);
//           });
//           setTimeout(adjustNameColumnWidth, 0);
//           initializeSorting();
//         })
//         .catch(error => {
//           console.error('Error loading table data:', error);
//           document.querySelector('#mmmu-table tbody').innerHTML = `
//             <tr>
//                 <td colspan="21"> Error loading data: ${error.message}<br> Please ensure you're accessing this page through a web server (http://localhost:8000) and not directly from the file system. </td>
//             </tr>
//           `;
//         });
//   }

// function setupEventListeners() {
//   document.querySelector('.reset-cell').addEventListener('click', function() {
//     resetTable();
//   });

//   document.querySelector('.pro-details-cell').addEventListener('click', function() {
//     toggleDetails('pro');
//   });
//   document.querySelector('.val-details-cell').addEventListener('click', function() {
//     toggleDetails('val');
//   });
//   document.querySelector('.test-details-cell').addEventListener('click', function() {
//     toggleDetails('test');
//   });

//   var headers = document.querySelectorAll('#mmmu-table thead tr:last-child th.sortable');
//   headers.forEach(function(header) {
//     header.addEventListener('click', function() {
//       sortTable(this);
//     });
//   });
// }

// function toggleDetails(section) {
//   var sections = ['pro', 'val', 'test'];
//   sections.forEach(function(sec) {
//     var detailCells = document.querySelectorAll('.' + sec + '-details');
//     var overallCells = document.querySelectorAll('.' + sec + '-overall');
//     var headerCell = document.querySelector('.' + sec + '-details-cell');
//     if (sec === section) {
//       detailCells.forEach(cell => cell.classList.toggle('hidden'));
//       headerCell.setAttribute('colspan', headerCell.getAttribute('colspan') === '1' ? (sec === 'pro' ? '3' : '7') : '1');
//     } else {
//       detailCells.forEach(cell => cell.classList.add('hidden'));
//       overallCells.forEach(cell => cell.classList.remove('hidden'));
//       headerCell.setAttribute('colspan', '1');
//     }
//   });

//   setTimeout(adjustNameColumnWidth, 0);
// }

// function resetTable() {
//   document.querySelectorAll('.pro-details, .val-details, .test-details').forEach(function(cell) {
//     cell.classList.add('hidden');
//   });

//   document.querySelectorAll('.pro-overall, .val-overall, .test-overall').forEach(function(cell) {
//     cell.classList.remove('hidden');
//   });

//   document.querySelector('.pro-details-cell').setAttribute('colspan', '1');
//   document.querySelector('.val-details-cell').setAttribute('colspan', '1');
//   document.querySelector('.test-details-cell').setAttribute('colspan', '1');

//   var valOverallHeader = document.querySelector('#mmmu-table thead tr:last-child th.val-overall');
//   sortTable(valOverallHeader, true);

//   setTimeout(adjustNameColumnWidth, 0);
// }

// function sortTable(header, forceDescending = false, maintainOrder = false) {
//   var table = document.getElementById('mmmu-table');
//   var tbody = table.querySelector('tbody');
//   var rows = Array.from(tbody.querySelectorAll('tr'));
//   var headers = Array.from(header.parentNode.children);
//   var columnIndex = headers.indexOf(header);
//   var sortType = header.dataset.sort;

//   var isDescending = forceDescending || (!header.classList.contains('asc') && !header.classList.contains('desc')) || header.classList.contains('asc');

//   if (!maintainOrder) {
//     rows.sort(function(a, b) {
//       var aValue = getCellValue(a, columnIndex);
//       var bValue = getCellValue(b, columnIndex);

//       if (aValue === '-' && bValue !== '-') return isDescending ? 1 : -1;
//       if (bValue === '-' && aValue !== '-') return isDescending ? -1 : 1;

//       if (sortType === 'number') {
//         return isDescending ? parseFloat(bValue) - parseFloat(aValue) : parseFloat(aValue) - parseFloat(bValue);
//       } else if (sortType === 'date') {
//         return isDescending ? new Date(bValue) - new Date(aValue) : new Date(aValue) - new Date(bValue);
//       } else {
//         return isDescending ? bValue.localeCompare(aValue) : aValue.localeCompare(bValue);
//       }
//     });
//   }

//   headers.forEach(function(th) {
//     th.classList.remove('asc', 'desc');
//   });

//   header.classList.add(isDescending ? 'desc' : 'asc');

//   rows.forEach(function(row) {
//     tbody.appendChild(row);
//   });

//   setTimeout(adjustNameColumnWidth, 0);
// }

// function getCellValue(row, index) {
//   var cells = Array.from(row.children);
//   var cell = cells[index];

//   if (cell.classList.contains('hidden')) {
//     if (cell.classList.contains('pro-details') || cell.classList.contains('pro-overall')) {
//       cell = cells.find(c => (c.classList.contains('pro-overall') || c.classList.contains('pro-details')) && !c.classList.contains('hidden'));
//     } else if (cell.classList.contains('val-details') || cell.classList.contains('val-overall')) {
//       cell = cells.find(c => (c.classList.contains('val-overall') || c.classList.contains('val-details')) && !c.classList.contains('hidden'));
//     } else if (cell.classList.contains('test-details') || cell.classList.contains('test-overall')) {
//       cell = cells.find(c => (c.classList.contains('test-overall') || c.classList.contains('test-details')) && !c.classList.contains('hidden'));
//     }
//   }
//   return cell ? cell.textContent.trim() : '';
// }

// function initializeSorting() {
//   var valOverallHeader = document.querySelector('#mmmu-table thead tr:last-child th.val-overall');
//   sortTable(valOverallHeader, true);
// }

// function adjustNameColumnWidth() {
//   const nameColumn = document.querySelectorAll('#mmmu-table td:first-child, #mmmu-table th:first-child');
//   let maxWidth = 0;

//   const span = document.createElement('span');
//   span.style.visibility = 'hidden';
//   span.style.position = 'absolute';
//   span.style.whiteSpace = 'nowrap';
//   document.body.appendChild(span);

//   nameColumn.forEach(cell => {
//     span.textContent = cell.textContent;
//     const width = span.offsetWidth;
//     if (width > maxWidth) {
//       maxWidth = width;
//     }
//   });

//   document.body.removeChild(span);

//   maxWidth += 20; // Increased padding

//   nameColumn.forEach(cell => {
//     cell.style.width = `${maxWidth}px`;
//     cell.style.minWidth = `${maxWidth}px`; // Added minWidth
//     cell.style.maxWidth = `${maxWidth}px`;
//   });
// }

// function prepareScoresForStyling(data, section) {
//   const scores = {};
//   const fields = [
//     'overall', 'vision', 'original', 'artDesign', 'business',
//     'science', 'healthMedicine', 'humanSocialSci', 'techEng'
//   ];

//   fields.forEach(field => {
//     const values = data.map(row => row[section] && row[section][field])
//                        .filter(value => value !== '-' && value !== undefined && value !== null)
//                        .map(parseFloat);

//     if (values.length > 0) {
//       const sortedValues = [...new Set(values)].sort((a, b) => b - a);
//       scores[field] = data.map(row => {
//         const value = row[section] && row[section][field];
//         if (value === '-' || value === undefined || value === null) {
//           return -1;
//         }
//         return sortedValues.indexOf(parseFloat(value));
//       });
//     } else {
//       scores[field] = data.map(() => -1);
//     }
//   });

//   return scores;
// }

// function applyStyle(value, rank) {
//       if (value === undefined || value === null || value === '-') return '-';
//       if (rank === 0) return `<b>${value}</b>`;
//       if (rank === 1) return `<span style="text-decoration: underline;">${value}</span>`;
//       return value;
// }


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
  setupEventListeners();
  window.addEventListener('resize', adjustNameColumnWidth);
});

const modelNameMapping = {
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
  'GPT-4o (0513)', 'Claude-3.5-Sonnet', 'Gemini-1.5-Pro-002', 
  'Qwen2-VL-72B', 'InternVL2-Llama3-76B', 'LLaVA-OneVision-72B'
]);

function loadTableData() {
  fetch('./static/data/full_results.json')
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
          const coreNonCotScores = prepareScoresForStyling(Object.values(data).map(model => model.core_noncot.macro_mean_score));
          const coreCotScores = prepareScoresForStyling(Object.values(data).map(model => model.core_cot.macro_mean_score));
          const openScores = prepareScoresForStyling(Object.values(data).map(model => model.open.macro_mean_score));

          Object.entries(data).forEach(([modelKey, modelData], index) => {
              const modelName = modelNameMapping[modelKey] || modelKey;
              const tr = document.createElement('tr');
              tr.classList.add(getModelTypeClass(modelName));
              tr.innerHTML = `
                  <td>${modelName}</td>
                  <td class="overall-score">${applyStyle(modelData.overall_score.toFixed(4), overallScores[index])}</td>
                  <td class="core-noncot-overall">${applyStyle(modelData.core_noncot.macro_mean_score.toFixed(4), coreNonCotScores[index])}</td>
                  <td class="hidden core-noncot-details">${modelData.core_noncot.macro_mean_score.toFixed(4)}</td>
                  <td class="hidden core-noncot-details">${modelData.core_noncot.micro_mean_score.toFixed(4)}</td>
                  <td class="core-cot-overall">${applyStyle(modelData.core_cot.macro_mean_score.toFixed(4), coreCotScores[index])}</td>
                  <td class="hidden core-cot-details">${modelData.core_cot.macro_mean_score.toFixed(4)}</td>
                  <td class="hidden core-cot-details">${modelData.core_cot.micro_mean_score.toFixed(4)}</td>
                  <td class="open-overall">${applyStyle(modelData.open.macro_mean_score.toFixed(4), openScores[index])}</td>
                  <td class="hidden open-details">${modelData.open.macro_mean_score.toFixed(4)}</td>
                  <td class="hidden open-details">${modelData.open.micro_mean_score.toFixed(4)}</td>
              `;
              tbody.appendChild(tr);
          });

          setTimeout(adjustNameColumnWidth, 0);
          initializeSorting();
      })
      .catch(error => {
          console.error('Error loading table data:', error);
          document.querySelector('#mmmu-table tbody').innerHTML = `
              <tr>
                  <td colspan="11">Error loading data: ${error.message}</td>
              </tr>
          `;
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

function setupEventListeners() {
  document.querySelector('.reset-cell').addEventListener('click', function() {
    resetTable();
  });

  ['core-noncot', 'core-cot', 'open'].forEach(section => {
    document.querySelector(`.${section}-details-cell`).addEventListener('click', function() {
      toggleDetails(section);
    });
  });

  var headers = document.querySelectorAll('#mmmu-table thead tr:last-child th.sortable');
  headers.forEach(function(header) {
    header.addEventListener('click', function() {
      sortTable(this);
    });
  });
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
  var overallScoreHeader = document.querySelector('#mmmu-table thead tr:last-child th.overall-score');
  sortTable(overallScoreHeader, true);
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