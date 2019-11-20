const psChartA = new Chart(document.querySelector("#ps-chart-1 > canvas"), {
  "type":"radar",
  "data":{
    "labels":[
      ["A1.1.", "Oog voor ontwikkeling"],
      ["A1.2.", "Pedagogische aanpak"],
      ["A2.1.", "Regels en afspraken"],
      ["A2.2.", "Groepsvorming"],
      ["A3.1.", "Democratie en", "participatie"],
      ["A3.2.", "Identiteitsontwikkeling"]
    ],
    "datasets":[{
      "label":"Categorie niveau",
      "data":[
        psLevelValues["level_A_1_1"],
        psLevelValues["level_A_1_2"],
        psLevelValues["level_A_2_1"],
        psLevelValues["level_A_2_2"],
        psLevelValues["level_A_3_1"],
        psLevelValues["level_A_3_2"]
      ]
    }]
  },
  "options":{
    "scale": {
      "pointLabels": {
        "fontSize": 14
      },
      "ticks": {
        "min": 0,
        "max": 5,
        "stepSize": 1,
        "callback": function(value, index, values) {
          switch(value) {
            case 1:
              return "Beginnend";
            case 2:
              return "In ontwikkeling";
            case 3:
              return "Startbekwaam";
            case 4:
              return "Basisbekwaam";
            case 5:
              return "Vakbekwaam";
            default:
              return "error - undefined value";
          }
        }
      }
    },
    "elements":{
      "line":{"tension":0,"borderWidth":3}
    }
  }
});


const psChartB = new Chart(document.querySelector("#ps-chart-2 > canvas"), {
  "type":"radar",
  "data":{
    "labels":[
      ["B1.1.", "Vakkennis en", "vaardigheden"],
      ["B1.2.", "Inzicht in leerlijnen"],
      ["B2.1.", "Verdiepen in", "een vakgebied"],
      ["B2.2.", "Geïntegreerd werken"],
      ["B3.1.", "Leerstof afstemmen"],
      ["B3.2.", "Leerstof en context"]
    ],
    "datasets":[{
      "label":"Categorie niveau",
      "data":[
        psLevelValues["level_B_1_1"],
        psLevelValues["level_B_1_2"],
        psLevelValues["level_B_2_1"],
        psLevelValues["level_B_2_2"],
        psLevelValues["level_B_3_1"],
        psLevelValues["level_B_3_2"]
      ]
    }]
  },
  "options":{
    "scale": {
      "pointLabels": {
        "fontSize": 14
      },
      "ticks": {
        "min": 0,
        "max": 5,
        "stepSize": 1,
        "callback": function(value, index, values) {
          switch(value) {
            case 1:
              return "Beginnend";
            case 2:
              return "In ontwikkeling";
            case 3:
              return "Startbekwaam";
            case 4:
              return "Basisbekwaam";
            case 5:
              return "Vakbekwaam";
            default:
              return "error - undefined value";
          }
        }
      }
    },
    "elements":{
      "line":{"tension":0,"borderWidth":3}
    }
  }
});



const psChartC = new Chart(document.querySelector("#ps-chart-3 > canvas"), {
  "type":"radar",
  "data":{
    "labels":[
      ["C1.1", "Leerlingen volgen"],
      ["C1.2", "Ontwikkeling", "leerlingen analyseren"],
      ["C2.1", "Onderwijs ontwerpen"],
      ["C2.2", "Aansprekend uitleggen"],
      ["C3.1", "Activeren van kennis"],
      ["C3.2", "Activiteiten afstemmen"]
    ],
    "datasets":[{
      "label":"Categorie niveau",
      "data":[
        psLevelValues["level_C_1_1"],
        psLevelValues["level_C_1_2"],
        psLevelValues["level_C_2_1"],
        psLevelValues["level_C_2_2"],
        psLevelValues["level_C_3_1"],
        psLevelValues["level_C_3_2"]
      ]
    }]
  },
  "options":{
    "scale": {
      "pointLabels": {
        "fontSize": 14
      },
      "ticks": {
        "min": 0,
        "max": 5,
        "stepSize": 1,
        "callback": function(value, index, values) {
          switch(value) {
            case 1:
              return "Beginnend";
            case 2:
              return "In ontwikkeling";
            case 3:
              return "Startbekwaam";
            case 4:
              return "Basisbekwaam";
            case 5:
              return "Vakbekwaam";
            default:
              return "error - undefined value";
          }
        }
      }
    },
    "elements":{
      "line":{"tension":0,"borderWidth":3}
    }
  }
});


const bpbChartD = new Chart(document.querySelector("#bpb-chart-1 > canvas"), {
  "type":"radar",
  "data":{
    "labels":[
      ["D1.1", "Beheer van ruimte"],
      ["D1.2", "Planning en tijd   "],
      ["D2.1", "Taakgerichte", "leeromgeving"],
      ["D2.2", "Overgangen en", "onderbrekingen"],
      ["D3.1", "Gebruik van materialen"],
      ["D3.2", "Samenwerking en", "activering"]
    ],
    "datasets":[{
      "label":"Categorie niveau",
      "data":[
        bpbLevelValues["level_D_1_1"],
        bpbLevelValues["level_D_1_2"],
        bpbLevelValues["level_D_2_1"],
        bpbLevelValues["level_D_2_2"],
        bpbLevelValues["level_D_3_1"],
        bpbLevelValues["level_D_3_2"]
      ]
    }]
  },
  "options":{
    "scale": {
      "pointLabels": {
        "fontSize": 14
      },
      "ticks": {
        "min": 0,
        "max": 5,
        "stepSize": 1,
        "callback": function(value, index, values) {
          switch(value) {
            case 1:
              return "Beginnend";
            case 2:
              return "In ontwikkeling";
            case 3:
              return "Startbekwaam";
            case 4:
              return "Basisbekwaam";
            case 5:
              return "Vakbekwaam";
            default:
              return "error - undefined value";
          }
        }
      }
    },
    "elements":{
      "line":{"tension":0,"borderWidth":3}
    }
  }
});


const bpbChartE = new Chart(document.querySelector("#bpb-chart-2 > canvas"), {
  "type":"radar",
  "data":{
    "labels":[
      ["E1.1", "Overzicht"],
      ["E1.2", "Overwicht"],
      ["E2.1", "(Non)verbale houding"],
      ["E2.2", "Gespreksvaardigheden"],
      ["E3.1", "Open houding"],
      ["E3.2", "Empathie"]
    ],
    "datasets":[{
      "label":"Categorie niveau",
      "data":[
        bpbLevelValues["level_E_1_1"],
        bpbLevelValues["level_E_1_2"],
        bpbLevelValues["level_E_2_1"],
        bpbLevelValues["level_E_2_2"],
        bpbLevelValues["level_E_3_1"],
        bpbLevelValues["level_E_3_2"]
      ]
    }]
  },
  "options":{
    "scale": {
      "pointLabels": {
        "fontSize": 14
      },
      "ticks": {
        "min": 0,
        "max": 5,
        "stepSize": 1,
        "callback": function(value, index, values) {
          switch(value) {
            case 1:
              return "beginnend";
            case 2:
              return "In ontwikkeling";
            case 3:
              return "Startbekwaam";
            case 4:
              return "Basisbekwaam";
            case 5:
              return "Vakbekwaam";
            default:
              return "error - undefined value";
          }
        }
      }
    },
    "elements":{
      "line":{"tension":0,"borderWidth":3}
    }
  }
});



const bpbChartF = new Chart(document.querySelector("#bpb-chart-3 > canvas"), {
  "type":"radar",
  "data":{
    "labels":[
      ["F1.1", "Collegiale consultatie", "en intervisie"],
      ["F1.2", "Advies vragen", "en bieden"],
      ["F2.1", "Communicatie met ouders"],
      ["F2.2", "Educatieve samenwerking"],
      ["F3.1", "Contact onderwijs", "en opvoeding"]
    ],
    "datasets":[{
      "label":"Categorie niveau",
      "data":[
        bpbLevelValues["level_F_1_1"],
        bpbLevelValues["level_F_1_2"],
        bpbLevelValues["level_F_2_1"],
        bpbLevelValues["level_F_2_2"],
        bpbLevelValues["level_F_3_1"]
      ]
    }]
  },
  "options":{
    "scale": {
      "pointLabels": {
        "fontSize": 14
      },
      "ticks": {
        "min": 0,
        "max": 5,
        "stepSize": 1,
        "callback": function(value, index, values) {
          switch(value) {
            case 1:
              return "Beginnend";
            case 2:
              return "In ontwikkeling";
            case 3:
              return "Startbekwaam";
            case 4:
              return "Basisbekwaam";
            case 5:
              return "Vakbekwaam";
            default:
              return "error - undefined value";
          }
        }
      }
    },
    "elements":{
      "line":{"tension":0,"borderWidth":3}
    }
  }
});



const bpbChartG = new Chart(document.querySelector("#bpb-chart-4 > canvas"), {
  "type":"radar",
  "data":{
    "labels":[
      ["G1.1", "Onderzoeksvaardigheden"],
      ["G1.2", "Onderzoekende", "houding"],
      ["G2.1", "Omgaan met feedback"],
      ["G2.2", "Eigen handelen", "analyseren"],
      ["G3.1", " Koppeling theorie", "en praktijk"],
      ["G3.2", "Persoonlijke", " leerdoelen", "formuleren"]
    ],
    "datasets":[{
      "label":"Categorie niveau",
      "data":[
        bpbLevelValues["level_G_1_1"],
        bpbLevelValues["level_G_1_2"],
        bpbLevelValues["level_G_2_1"],
        bpbLevelValues["level_G_2_2"],
        bpbLevelValues["level_G_3_1"],
        bpbLevelValues["level_G_3_2"]
      ]
    }]
  },
  "options":{
    "scale": {
      "pointLabels": {
        "fontSize": 14
      },
      "ticks": {
        "min": 0,
        "max": 5,
        "stepSize": 1,
        "callback": function(value, index, values) {
          switch(value) {
            case 1:
              return "Beginnend";
            case 2:
              return "In ontwikkeling";
            case 3:
              return "Startbekwaam";
            case 4:
              return "Basisbekwaam";
            case 5:
              return "Vakbekwaam";
            default:
              return "error - undefined value";
          }
        }
      }
    },
    "elements":{
      "line":{"tension":0,"borderWidth":3}
    }
  },
});
