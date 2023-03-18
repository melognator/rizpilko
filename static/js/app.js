function ajaxRedirect(certainPath) {
  return $.ajax({
    url: certainPath,
    type: 'GET',
    success: function(data) {
      $('#main-content').replaceWith(data)
    }
  });
}

function redirectHome(e) {
  $('#main-content').replaceWith(home)
  deselectNavbarElements();
  document.getElementById("navbarHome").classList.add('filter-blue');
  document.getElementById("navbarHome").classList.remove('hover-blue');
  document.getElementById("sidebarText").innerHTML = "¡Bienvenido otra vez, " + usuario[0][1] + "! Espero que tengas un buen día.";
  actualizarXP();
  try {
    e.preventDefault();
  } catch (error) {
    
  }
  
}

function actualizarXP() {
  nivel = Math.floor(usuario[0][2]/100)+1
  experiencia = usuario[0][2]%100
  document.getElementById("nivel").innerHTML = `Nivel ${nivel}`;
  document.getElementById("xp").innerHTML = `${experiencia} / 100`;
}

function redirectTareas(e) {
  $('#main-content').replaceWith(tareas)
  deselectNavbarElements();
  document.getElementById("navbarTareas").classList.add('filter-blue');
  document.getElementById("navbarTareas").classList.remove('hover-blue');
  document.getElementById("sidebarText").innerHTML = "Aquí se encuentran las tareas (sin repetición) que tengas";
  e.preventDefault();
}

function redirectCalendario(e) {
  $('#main-content').replaceWith(calendario)
  deselectNavbarElements();
  document.getElementById("navbarCalendario").classList.add('filter-blue');
  document.getElementById("navbarCalendario").classList.remove('hover-blue');
  document.getElementById("sidebarText").innerHTML = "Aquí se encuentran los eventos o tareas recurrentes que tengas";
  e.preventDefault();
}

function redirectTemporizador(e) {
  $('#main-content').replaceWith(temporizador)
  deselectNavbarElements();
  document.getElementById("navbarTemporizador").classList.add('filter-green');
  document.getElementById("navbarTemporizador").classList.remove('hover-green');
  document.getElementById("sidebarText").innerHTML = "Haz click en inciar para iniciar el temporizador <br><br>Haz click en detener para detener el temporizador";
  e.preventDefault();
}

function redirectPomodoro(e) {
  $('#main-content').replaceWith(pomodoro)
  deselectNavbarElements();
  document.getElementById("navbarPomodoro").classList.add('filter-red');
  document.getElementById("navbarPomodoro").classList.remove('hover-red');
  document.getElementById("sidebarText").innerHTML = "Configura los tiempos y dale al botón del tomate para iniciar";
  e.preventDefault();
}

function redirectDiario(e) {
  $('#main-content').replaceWith(diario)
  deselectNavbarElements();
  document.getElementById("navbarDiario").classList.add('filter-yellow');
  document.getElementById("navbarDiario").classList.remove('hover-yellow');
  document.getElementById("sidebarText").innerHTML = "Haz click en las entradas para ver lo que escribiste";
  e.preventDefault();
}

function redirectConfiguracion(e) {
  $('#main-content').replaceWith(configuracion)
  deselectNavbarElements();
  document.getElementById("navbarConfiguracion").classList.add('filter-blue');
  document.getElementById("navbarConfiguracion").classList.remove('hover-blue');
  document.getElementById("sidebarText").innerHTML = "";
  e.preventDefault();
}

function deselectNavbarElements() {
  var children = document.getElementById("navbar").children;
  children[0].classList.remove('filter-blue');
  children[0].classList.add('hover-blue');
  children[1].classList.remove('filter-blue');
  children[1].classList.add('hover-blue');
  children[2].classList.remove('filter-blue');
  children[2].classList.add('hover-blue');
  children[3].classList.remove('filter-green');
  children[3].classList.add('hover-green');
  children[4].classList.remove('filter-red');
  children[4].classList.add('hover-red');
  children[5].classList.remove('filter-yellow');
  children[5].classList.add('hover-yellow');
  children[6].classList.remove('filter-blue');
  children[6].classList.add('hover-blue');
}


function onlyNumberKey(evt) {
    var ASCIICode = (evt.which) ? evt.which : evt.keyCode
    if (ASCIICode > 31 && (ASCIICode < 48 || ASCIICode > 57))
        return false;
    return true;
}

$(document).keyup(function(event) {
  
  if ($("#tarea-input").is(":focus") && event.key == "Enter") {
    var cantidadTareas = parseInt($("#cantidadTareas").val())
    var listaCategorias = $("#listaCategorias").val().split(",")
    listaCategorias[0] = listaCategorias[0].substring(2, listaCategorias[0].length);
    listaCategorias.pop();
    var htmlCategorias = "";
    listaCategorias.forEach(function(categoria, j, array) {
      if (j == 0) {
        htmlCategorias += `<option class="black-font" value="${j}" selected>${categoria}</option>`;
      } else {
        htmlCategorias += `<option class="black-font" value="${j}">${categoria}</option>`;
      }
    })
    var tituloTarea = $("#tarea-input").val();
    tr = `
      <div id="rowTarea${cantidadTareas}" class="row gray-bg m-2 m-sm-3 m-md-4" data-bs-toggle="modal" data-bs-target="#modalTarea${cantidadTareas}">
        <div class="col p-0">
          <div class="form-check d-flex align-items-center p-0">
            <input onclick="marcarCompletada(${cantidadTareas}, 'tareas'); closeModal('tareas');" class="form-check-input rounded-0 m-2 m-sm-2 m-md-3" type="checkbox" value="">
            <label class="form-check-label" for="homeTarea${cantidadTareas}">
              <span class="ink-font m-0 unselectable">${tituloTarea}</span>
            </label>
          </div>
        </div>
        <div class="col-4 m-2 m-sm-2 m-md-3 p-0 d-flex flex-row-reverse align-items-center">
          <span class="baja dot mb-0 unselectable d-inline-block"></span>
          <span class="roboto-font mb-0 unselectable d-inline-block me-2 me-sm-3 me-md-4 "></span>
        </div>
      </div>

      <div class="modal fade" id="modalTarea${cantidadTareas}" tabindex="-1" role="dialog" aria-labelledby="titleTarea" aria-hidden="true" data-bs-backdrop="static" data-bs-keyboard="false">
        <div class="modal-dialog modal-xl modal-dialog-centered modal-dialog-scrollable" role="document">
          <div class="modal-content abm-popup-background">
            <button type="button" class="btn-close p-0 ms-auto me-1 shadow-none" data-bs-dismiss="modal" aria-label="Close">
                <span class="unselectable roboto-font boton-cerrar" aria-hidden="true">&times;</span>
              </button>
            <div class="modal-header ms-2 ms-sm-3 ms-md-4 me-2 me-sm-3 me-md-4 mb-1 mb-md-2 p-0 d-flex flex-column align-items-baseline">
              <!-- <h5 class="modal-title" id="exampleModalLongTitle">titulo de la tarea</h5> -->
              <input id="titleTarea${cantidadTareas}" type="text" maxlength="64" size="64" class="m-0 ink-font" value="${$("#tarea-input").val()}" placeholder="Título de la tarea...">
              <div id="prioridadTarea${cantidadTareas}" class="d-flex flex-row align-items-center">
                <span class="ink-font m-0 unselectable me-1 me-md-2">Prioridad:</span>
                
                <a href="javascript:seleccionarPrioridad('prioridadTarea${cantidadTareas}', 0);" class="baja dot mb-0 unselectable d-inline-block ms-1"></a>
                <a href="javascript:seleccionarPrioridad('prioridadTarea${cantidadTareas}', 1);" class="media filter-gray dot mb-0 unselectable d-inline-block ms-1"></a>
                <a href="javascript:seleccionarPrioridad('prioridadTarea${cantidadTareas}', 2);" class="alta filter-gray dot mb-0 unselectable d-inline-block ms-1"></a>
              </div>
              <div class="d-flex flex-row align-items-center mb-1 mb-md-2">
                <span class="ink-font m-0 unselectable me-1 me-md-2">Categoría: </span>
                <select id="categoriaTarea${cantidadTareas}"class="ms-1 p-0 transparent-background ink-font shadow-none rounded-0" aria-label="">
                  ${htmlCategorias}
                </select>
              </div>
            </div>
            <div class="modal-body ms-2 ms-sm-3 ms-md-4 me-2 me-sm-3 me-md-4 mb-1 mb-md-2 p-0 d-flex flex-column align-items-baseline">
              <span class="ink-font m-0 unselectable me-1 me-md-2">Descripción: </span>
              <textarea class="w-100 m-0 shadow-none rounded-0 unselectable ink-font transparent-background" id="descTarea${cantidadTareas}" rows="3" placeholder="Escribe aquí una descripción..."></textarea>
              <div class="d-flex flex-row align-items-center">
                <span class="ink-font m-0 unselectable me-1 me-md-2">Fecha de recordatorio:</span>
                <input id="recordatorioTarea${cantidadTareas}" type="text" maxlength="64" size="24" class="m-0 roboto-font" value="" placeholder="Ejemplo: 24/10/2022 15:20:00">
              </div>
              <div class="d-flex flex-row align-items-center">
                <span class="ink-font m-0 unselectable me-1 me-md-2">Fecha límite:</span>
                <input id="limiteTarea${cantidadTareas}" type="text" maxlength="64" size="24" class="m-0 roboto-font" value="" placeholder="Ejemplo: 24/10/2022 15:20:00">
              </div>
            </div>
            <div class="modal-footer ms-2 ms-sm-3 ms-md-4 me-2 me-sm-3 me-md-4 mb-1 mb-md-2 p-0 d-flex flex-column align-items-baseline">
              <a href="javascript:guardarTarea(${cantidadTareas});" class="btn btn-outline-light ms-0 me-0 mb-1 mb-md-2 mt-2 mt-md-3 roboto-font rounded-0 p-1 p-md-2 shadow-none w-100" aria-label="Close">Guardar tarea</a>
              <a href="javascript:marcarCompletada(${cantidadTareas}, 'tareas');" class="btn btn-outline-light ms-0 me-0 mb-1 mb-md-2 roboto-font rounded-0 p-1 p-md-2 shadow-none w-100" aria-label="Close">Marcar tarea como completada</a>
              <a href="javascript:eliminarTarea(${cantidadTareas}, 'tareas');" class="btn btn-danger ms-0 me-0 mb-2 mb-md-3 roboto-font rounded-0 p-1 p-md-2 shadow-none w-100" aria-label="Close">Eliminar tarea</a>
            </div>
          </div>
        </div>
      </div>

      <input id="tareaID${cantidadTareas}" type="hidden" value=""></input>
    `


      $("#tareas-sin-completar").append(tr);
      $("#tarea-input").val('');
      var id_token = auth2.currentUser.get().getAuthResponse(true).id_token
      $.ajax({
        url: '/tareas/create',
        type: 'POST',
        data: JSON.stringify({
          token: id_token,
          titulo: tituloTarea
        }),
        contentType: "application/json; charset=utf-8",
        traditional: true,
        success: function(data) {
          $(`#tareaID${cantidadTareas}`).val(`${data}`)
        }
      })
      .done(function() {
        $("#cantidadTareas").val((cantidadTareas + 1).toString())
        tareas = $("#main-content").outerHTML();
      });
      $.ajax({
        url: '/usuario/incrementar-xp',
        type: 'POST',
        data: JSON.stringify({
          token: id_token,
          xp: 10
        }),
        contentType: "application/json; charset=utf-8",
        traditional: true,
        success: function(data) {
          usuario[0][2] += 10;
          actualizarXP();
        }
      });
    }
});

$(document).keyup(function(event) {
  
  if ($("#evento-input").is(":focus") && event.key == "Enter") {
    var cantidadTareas = parseInt($("#cantidadTareas").val())
    var listaCategorias = $("#listaCategorias").val().split(",")
    listaCategorias[0] = listaCategorias[0].substring(2, listaCategorias[0].length);
    listaCategorias.pop();
    var htmlCategorias = "";
    listaCategorias.forEach(function(categoria, j, array) {
      if (j == 0) {
        htmlCategorias += `<option class="black-font" value="${j}" selected>${categoria}</option>`;
      } else {
        htmlCategorias += `<option class="black-font" value="${j}">${categoria}</option>`;
      }
    })
    var tituloTarea = $("#evento-input").val();
    tr = `
      <div id="rowTarea${cantidadTareas}" class="row gray-bg m-2 m-sm-3 m-md-4" data-bs-toggle="modal" data-bs-target="#modalTarea${cantidadTareas}">
        <div class="col p-0">
          <div class="form-check d-flex align-items-center p-0">
            <input onclick="marcarCompletada(${cantidadTareas}, 'calendario'); closeModal('calendario');" class="form-check-input rounded-0 m-2 m-sm-2 m-md-3" type="checkbox" value="">
            <label class="form-check-label" for="homeTarea${cantidadTareas}">
              <span class="ink-font m-0 unselectable">${tituloTarea}</span>
            </label>
          </div>
        </div>
        <div class="col-4 m-2 m-sm-2 m-md-3 p-0 d-flex flex-row-reverse align-items-center">
          <span class="baja dot mb-0 unselectable d-inline-block"></span>
          <span class="roboto-font mb-0 unselectable d-inline-block me-2 me-sm-3 me-md-4 "></span>
        </div>
      </div>

      <div class="modal fade" id="modalTarea${cantidadTareas}" tabindex="-1" role="dialog" aria-labelledby="titleTarea" aria-hidden="true" data-bs-backdrop="static" data-bs-keyboard="false">
        <div class="modal-dialog modal-xl modal-dialog-centered modal-dialog-scrollable" role="document">
          <div class="modal-content abm-popup-background">
            <button type="button" class="btn-close p-0 ms-auto me-1 shadow-none" data-bs-dismiss="modal" aria-label="Close">
                <span class="unselectable roboto-font boton-cerrar" aria-hidden="true">&times;</span>
              </button>
            <div class="modal-header ms-2 ms-sm-3 ms-md-4 me-2 me-sm-3 me-md-4 mb-1 mb-md-2 p-0 d-flex flex-column align-items-baseline">
              <!-- <h5 class="modal-title" id="exampleModalLongTitle">titulo de la tarea</h5> -->
              <input id="titleTarea${cantidadTareas}" type="text" maxlength="64" size="64" class="m-0 ink-font" value="${$("#evento-input").val()}" placeholder="Título de la tarea...">
              <div id="prioridadTarea${cantidadTareas}" class="d-flex flex-row align-items-center">
                <span class="ink-font m-0 unselectable me-1 me-md-2">Prioridad:</span>
                
                <a href="javascript:seleccionarPrioridad('prioridadTarea${cantidadTareas}', 0);" class="baja dot mb-0 unselectable d-inline-block ms-1"></a>
                <a href="javascript:seleccionarPrioridad('prioridadTarea${cantidadTareas}', 1);" class="media filter-gray dot mb-0 unselectable d-inline-block ms-1"></a>
                <a href="javascript:seleccionarPrioridad('prioridadTarea${cantidadTareas}', 2);" class="alta filter-gray dot mb-0 unselectable d-inline-block ms-1"></a>
              </div>
              <div class="d-flex flex-row align-items-center mb-1 mb-md-2">
                <span class="ink-font m-0 unselectable me-1 me-md-2">Categoría: </span>
                <select id="categoriaTarea${cantidadTareas}"class="ms-1 p-0 transparent-background ink-font shadow-none rounded-0" aria-label="">
                  ${htmlCategorias}
                </select>
              </div>
            </div>
            <div class="modal-body ms-2 ms-sm-3 ms-md-4 me-2 me-sm-3 me-md-4 mb-1 mb-md-2 p-0 d-flex flex-column align-items-baseline">
              <span class="ink-font m-0 unselectable me-1 me-md-2">Descripción: </span>
              <textarea class="w-100 m-0 shadow-none rounded-0 unselectable ink-font transparent-background" id="descTarea${cantidadTareas}" rows="3" placeholder="Escribe aquí una descripción..."></textarea>
              <div class="d-flex flex-row align-items-center">
                <span class="ink-font m-0 unselectable me-1 me-md-2">Fecha de recordatorio:</span>
                <input id="fechaComienzoTarea${cantidadTareas}" type="text" maxlength="64" size="24" class="m-0 roboto-font" value="" placeholder="Ejemplo: 24/10/2022 15:20:00">
              </div>
              <div class="d-flex flex-row align-items-center">
                <span class="ink-font m-0 unselectable me-1 me-md-2">Fecha límite:</span>
                <input id="recordatorioTarea${cantidadTareas}" type="text" maxlength="64" size="24" class="m-0 roboto-font" value="" placeholder="Ejemplo: 7d, 1d, 2d (WIP)">
              </div>
            </div>
            <div class="modal-footer ms-2 ms-sm-3 ms-md-4 me-2 me-sm-3 me-md-4 mb-1 mb-md-2 p-0 d-flex flex-column align-items-baseline">
              <a href="javascript:guardarEvento(${cantidadTareas});" class="btn btn-outline-light ms-0 me-0 mb-1 mb-md-2 mt-2 mt-md-3 roboto-font rounded-0 p-1 p-md-2 shadow-none w-100" aria-label="Close">Guardar evento</a>
              <a href="javascript:marcarCompletada(${cantidadTareas}, 'calendario');" class="btn btn-outline-light ms-0 me-0 mb-1 mb-md-2 roboto-font rounded-0 p-1 p-md-2 shadow-none w-100" aria-label="Close">Marcar evento como completado</a>
              <a href="javascript:eliminarTarea(${cantidadTareas}, 'calendario');" class="btn btn-danger ms-0 me-0 mb-2 mb-md-3 roboto-font rounded-0 p-1 p-md-2 shadow-none w-100" aria-label="Close">Eliminar evento</a>
            </div>
          </div>
        </div>
      </div>

      <input id="tareaID${cantidadTareas}" type="hidden" value=""></input>
    `;


      $("#tareas-sin-completar").append(tr);
      $("#evento-input").val('');
      var id_token = auth2.currentUser.get().getAuthResponse(true).id_token
      $.ajax({
        url: '/calendario/create',
        type: 'POST',
        data: JSON.stringify({
          token: id_token,
          titulo: tituloTarea
        }),
        contentType: "application/json; charset=utf-8",
        traditional: true,
        success: function(data) {
          $(`#tareaID${cantidadTareas}`).val(`${data}`)
        }
      })
      .done(function() {
        $("#cantidadTareas").val((cantidadTareas + 1).toString())
        tareas = $("#main-content").outerHTML();
      });
      $.ajax({
        url: '/usuario/incrementar-xp',
        type: 'POST',
        data: JSON.stringify({
          token: id_token,
          xp: 10
        }),
        contentType: "application/json; charset=utf-8",
        traditional: true,
        success: function(data) {
          usuario[0][2] += 10;
          actualizarXP();
        }
      });
    }
});


jQuery.fn.outerHTML = function() {
  return jQuery('<div />').append(this.eq(0).clone()).html();
};

function seleccionarPrioridad(contenedor, prioridad) {
  var prioridadButtons = document.getElementById(contenedor).getElementsByTagName("a");
  for (let i = 0; i < 3; i++) {
    prioridadButtons[i].classList.remove('filter-gray');
    prioridadButtons[i].classList.add('filter-gray');
  }
  prioridadButtons[prioridad].classList.remove('filter-gray');
}

const delay = ms => new Promise(res => setTimeout(res, ms));

const eliminarTarea = async (tarea_id, pestania) => {
  $('.btn-close').click(); 
  document.getElementById('modalTarea' + tarea_id).remove();
  document.getElementById('rowTarea' + tarea_id).remove();
  var actualTarea_id = $('#tareaID' + tarea_id).val();
  var id_token = auth2.currentUser.get().getAuthResponse(true).id_token
  $.ajax({
    url: '/tareas/delete',
    type: 'DELETE',
    data: JSON.stringify({
      token: id_token,
      tarea_id: actualTarea_id
    }),
    contentType: "application/json; charset=utf-8",
    traditional: true,
    success: function(data) {
      
    }
  });
  await delay(300);
  if (pestania == "tareas") {
    tareas = $("#main-content").outerHTML();
  } else if (pestania == "calendario") {
    calendario = $("#main-content").outerHTML();
  }
}

const marcarCompletada = async (tarea_id, pestania) => {
  $('.btn-close').click(); 
  var target = document.getElementById("rowTarea" + tarea_id).getElementsByClassName("form-check-input")[0];
  target.setAttribute("checked", "checked");
  target.setAttribute( "onClick", `desmarcarCompletada(${tarea_id}, "${pestania}"); closeModal("${pestania}");` );
  target = document.getElementById("modalTarea" + tarea_id).getElementsByClassName("btn-outline-light")[1];
  target.textContent = "Desmarcar tarea como completada"
  target.href = `javascript:desmarcarCompletada(${tarea_id}, "${pestania}");`
  $("#rowTarea" + tarea_id).appendTo("#tareas-completadas");
  $("#modalTarea" + tarea_id).appendTo("#tareas-completadas");
  var actualTarea_id = $('#tareaID' + tarea_id).val();
  var id_token = auth2.currentUser.get().getAuthResponse(true).id_token
  $.ajax({
    url: '/tareas/completar',
    type: 'POST',
    data: JSON.stringify({
      token: id_token,
      tarea_id: actualTarea_id
    }),
    contentType: "application/json; charset=utf-8",
    traditional: true,
    success: function(data) {
      
    }
  });
  $.ajax({
      url: '/usuario/incrementar-xp',
      type: 'POST',
      data: JSON.stringify({
        token: id_token,
        xp: 15
      }),
      contentType: "application/json; charset=utf-8",
      traditional: true,
      success: function(data) {
        usuario[0][2] += 15;
        actualizarXP();
      }
    });
  await delay(300);
  if (pestania == "tareas") {
    tareas = $("#main-content").outerHTML();
  } else if (pestania == "calendario") {
    calendario = $("#main-content").outerHTML();
  }
}


const desmarcarCompletada = async (tarea_id, pestania) => {
  $('.btn-close').click(); 
  var target = document.getElementById("rowTarea" + tarea_id).getElementsByClassName("form-check-input")[0];
  target.removeAttribute("checked");
  target.setAttribute( "onClick", `marcarCompletada(${tarea_id}, "${pestania}"); closeModal("${pestania}");` );
  target = document.getElementById("modalTarea" + tarea_id).getElementsByClassName("btn-outline-light")[1];
  target.textContent = "Marcar tarea como completada"
  target.href = `javascript:marcarCompletada(${tarea_id}, "${pestania}");`
  $("#rowTarea" + tarea_id).appendTo("#tareas-sin-completar");
  $("#modalTarea" + tarea_id).appendTo("#tareas-sin-completar");
  var actualTarea_id = $('#tareaID' + tarea_id).val();
  var id_token = auth2.currentUser.get().getAuthResponse(true).id_token
  $.ajax({
    url: '/tareas/descompletar',
    type: 'POST',
    data: JSON.stringify({
      token: id_token,
      tarea_id: actualTarea_id
    }),
    contentType: "application/json; charset=utf-8",
    traditional: true,
    success: function(data) {
      
    }
  });
  $.ajax({
    url: '/usuario/incrementar-xp',
    type: 'POST',
    data: JSON.stringify({
      token: id_token,
      xp: -15
    }),
    contentType: "application/json; charset=utf-8",
    traditional: true,
    success: function(data) {
      usuario[0][2] -= 15;
      actualizarXP();
    }
  });
  await delay(300);
  if (pestania == "tareas") {
    tareas = $("#main-content").outerHTML();
  } else if (pestania == "calendario") {
    calendario = $("#main-content").outerHTML();
  }
}

const guardarTarea = async (tarea_id) => {
  $('.btn-close').click(); 
  var target = document.getElementById("rowTarea" + tarea_id).getElementsByClassName("dot")[0];
  var titulo = $('#titleTarea' + tarea_id).val();
  var descripcion = $('#descTarea' + tarea_id).val();
  var fecha_limite = $('#limiteTarea' + tarea_id).val();
  var fecha_recordatorio = $('#recordatorioTarea' + tarea_id).val();
  var categoria = categorias[$('#categoriaTarea' + tarea_id).val()][0];
  var dotPrioridades = document.getElementById("modalTarea" + tarea_id).getElementsByClassName("dot");
  for (let i = 0, len = dotPrioridades.length; i < len; i++) {
    if (!dotPrioridades[i].classList.contains('filter-gray')) {
       var prioridad = i;
    }
  }
  target.classList.remove("alta", "media", "baja");
  var prioridades = ["baja", "media", "alta"];
  target.classList.add(prioridades[prioridad])
  target = document.getElementById("rowTarea" + tarea_id).getElementsByClassName("roboto-font")[0];
  target.innerHTML = fecha_limite;
  target = document.getElementById("rowTarea" + tarea_id).getElementsByClassName("ink-font")[0];
  target.innerHTML = titulo;
  var actualTarea_id = $('#tareaID' + tarea_id).val();
  var id_token = auth2.currentUser.get().getAuthResponse(true).id_token;
  $.ajax({
    url: '/tareas',
    type: 'PUT',
    data: JSON.stringify({
      token: id_token,
      tarea_id: actualTarea_id,
      titulo: titulo,
      categoria: categoria,
      descripcion: descripcion,
      prioridad: prioridad,
      fecha_limite: fecha_limite,
      fecha_recordatorio: fecha_recordatorio
    }),
    contentType: "application/json; charset=utf-8",
    traditional: true,
    success: function(data) {
      
    }
  });
  await delay(300);
  tareas = $("#main-content").outerHTML();
}

const guardarEvento = async (tarea_id) => {
  $('.btn-close').click(); 
  var target = document.getElementById("rowTarea" + tarea_id).getElementsByClassName("dot")[0];
  var titulo = $('#titleTarea' + tarea_id).val();
  var descripcion = $('#descTarea' + tarea_id).val();
  var frecuencia = $('#frecuenciaTarea' + tarea_id).val();
  var fecha_comienzo = $('#fechaComienzoTarea' + tarea_id).val();
  var categoria = categorias[$('#categoriaTarea' + tarea_id).val()][0];
  var dotPrioridades = document.getElementById("modalTarea" + tarea_id).getElementsByClassName("dot");
  for (let i = 0, len = dotPrioridades.length; i < len; i++) {
    if (!dotPrioridades[i].classList.contains('filter-gray')) {
       var prioridad = i;
    }
  }
  target.classList.remove("alta", "media", "baja");
  var prioridades = ["baja", "media", "alta"];
  target.classList.add(prioridades[prioridad])
  target = document.getElementById("rowTarea" + tarea_id).getElementsByClassName("roboto-font")[0];
  target.innerHTML = fecha_comienzo;
  target = document.getElementById("rowTarea" + tarea_id).getElementsByClassName("ink-font")[0];
  target.innerHTML = titulo;
  var actualTarea_id = $('#tareaID' + tarea_id).val();
  var id_token = auth2.currentUser.get().getAuthResponse(true).id_token;
  $.ajax({
    url: '/calendario',
    type: 'PUT',
    data: JSON.stringify({
      token: id_token,
      tarea_id: actualTarea_id,
      titulo: titulo,
      categoria: categoria,
      descripcion: descripcion,
      prioridad: prioridad,
      frecuencia: frecuencia,
      fecha_comienzo: fecha_comienzo
    }),
    contentType: "application/json; charset=utf-8",
    traditional: true,
    success: function(data) {
      
    }
  });
  await delay(300);
  calendario = $("#main-content").outerHTML();
}

const closeModal = async (pestania) => {
  await delay(500)
  $('.btn-close').click(); 
  await delay(300);
  if (pestania == "tareas") {
    tareas = $("#main-content").outerHTML();
  } else if (pestania == "calendario") {
    calendario = $("#main-content").outerHTML();
  }
  
}

function timeToString(time) {
  let diffInHrs = time / 3600000;
  let hh = Math.floor(diffInHrs);

  let diffInMin = (diffInHrs - hh) * 60;
  let mm = Math.floor(diffInMin);

  let diffInSec = (diffInMin - mm) * 60;
  let ss = Math.floor(diffInSec);

  let diffInMs = (diffInSec - ss) * 100;
  let ms = Math.floor(diffInMs);

  let formattedHH = hh.toString().padStart(2, "0");
  let formattedMM = mm.toString().padStart(2, "0");
  let formattedSS = ss.toString().padStart(2, "0");
  let formattedMS = ms.toString().padStart(2, "0");

  return `${formattedHH}:${formattedMM}:${formattedSS}`;
}

var startTime;
var elapsedTime = 0;
var timerInterval;

function iniciarTimer() {
  startTime = Date.now() - elapsedTime;
  $("#botonDetener").removeAttr('disabled');
  $("#botonIniciar").attr("disabled", true);
  timerInterval = setInterval(function printTime() {
    elapsedTime = Date.now() - startTime;
    try {
      document.getElementById("temporizadorSpan").innerHTML = timeToString(elapsedTime);
      temporizador = $("#main-content").outerHTML();
    } catch (error) {

    }
  }, 1000);
}

function timeNow(i) {
  i.value = new Date().toLocaleTimeString([], {hour: '2-digit', minute:'2-digit', second:'2-digit'});
}

function msToTime(duration) {
  var milliseconds = Math.floor((duration % 1000) / 100),
    seconds = Math.floor((duration / 1000) % 60),
    minutes = Math.floor((duration / (1000 * 60)) % 60),
    hours = Math.floor((duration / (1000 * 60 * 60)) % 24);

  hours = (hours < 10) ? "" + hours : hours;
  minutes = (minutes < 10) ? "0" + minutes : minutes;
  seconds = (seconds < 10) ? "0" + seconds : seconds;

  return hours + ":" + minutes + ":" + seconds;
}

function detenerTimer() {
  clearInterval(timerInterval);
  $("#botonDetener").attr('disabled', true);
  $("#botonIniciar").removeAttr('disabled');
  document.getElementById("temporizadorSpan").innerHTML = "00:00:00";
  tr = `
    <div class="row gray-bg m-2 m-sm-3 m-md-4 ps-1 ps-md-2 pe-1 pe-md-2">
      <div class="col p-1 m-1 m-md-2 d-flex flex-row">
        <span class="ink-font m-0 unselectable">${$("#actividad-input").val()}</span>
      </div>
      <div class="col-6 m-2 m-sm-2 m-md-3 p-0 d-flex flex-row-reverse align-items-center">
        <span class="roboto-font mb-0 unselectable d-inline-block">${msToTime(Date.now()-startTime)}</span>
        <span class="roboto-font mb-0 unselectable me-2 me-sm-3 me-md-4 d-inline-block">${new Date(startTime).toLocaleTimeString()} - ${new Date(Date.now()).toLocaleTimeString()}</span>
        <span class="roboto-font mb-0 unselectable me-2 me-sm-3 me-md-4 d-inline-block">${$("#categoriaActividad option:selected").text()}</span>
      </div>
    </div>
  `;
  var titulo = $("#actividad-input").val();
  var categoria = $("#categoriaActividad option:selected").val();
  var fecha_comienzo = (new Date(startTime).toLocaleDateString()).toString() + " " + (new Date(startTime).toLocaleTimeString()).toString();
  var fecha_fin = (new Date(Date.now()).toLocaleDateString()).toString() + " " + (new Date(Date.now()).toLocaleTimeString()).toString();
  var id_token = auth2.currentUser.get().getAuthResponse(true).id_token
  $("#actividades").append(tr);
  $("#actividad-input").val('')
  $.ajax({
    url: '/temporizador/create',
    type: 'POST',
    data: JSON.stringify({
      token: id_token,
      titulo: titulo,
      categoria: categoria,
      fecha_comienzo: fecha_comienzo,
      fecha_fin: fecha_fin
    }),
    contentType: "application/json; charset=utf-8",
    traditional: true,
    success: function(data) {
      
    }
  });
  $.ajax({
    url: '/usuario/incrementar-xp',
    type: 'POST',
    data: JSON.stringify({
      token: id_token,
      xp: 15
    }),
    contentType: "application/json; charset=utf-8",
    traditional: true,
    success: function(data) {
      usuario[0][2] += 15;
      actualizarXP();
    }
  });
  temporizador = $("#main-content").outerHTML();
  elapsedTime = 0;
}


$(document).keyup(function(event) {
  
  if ($("#entrada-input0").is(":focus") && event.key == "Enter") {
    var cantidadEntradas = parseInt($("#cantidadEntradas").val())
    var tituloEntrada = $("#entrada-input0").val();
    var todayDate = (new Date(Date.now()).toLocaleDateString()).toString() + " " + (new Date(Date.now()).toLocaleTimeString()).toString();
    tr = `
      <div id="rowEntrada${cantidadEntradas}" class="row gray-bg m-2 m-sm-3 m-md-4 ps-1 ps-md-2 pe-1 pe-md-2" data-bs-toggle="modal" data-bs-target="#modalEntrada${cantidadEntradas}">
        <div class="col p-1 m-1 m-md-2 p-0 d-flex flex-row">
          <span class="ink-font m-0 unselectable">${tituloEntrada}</span>
        </div>
        <div class="col-4 m-1 m-md-2 p-1 d-flex flex-row-reverse align-items-center">
          <span class="roboto-font mb-0 unselectable d-inline-block">${todayDate}</span>
        </div>
      </div>

      <div class="modal fade" id="modalEntrada${cantidadEntradas}" tabindex="-1" role="dialog" aria-labelledby="titleEntrada" aria-hidden="true" data-bs-backdrop="static" data-bs-keyboard="false">
        <div class="modal-dialog modal-xl modal-dialog-centered modal-dialog-scrollable" role="document">
          <div class="modal-content abm-popup-background">
            <button type="button" class="btn-close p-0 ms-auto me-1 shadow-none" data-bs-dismiss="modal" aria-label="Close">
                <span class="unselectable roboto-font boton-cerrar" aria-hidden="true">&times;</span>
              </button>
            <div class="modal-header ms-2 ms-sm-3 ms-md-4 me-2 me-sm-3 me-md-4 mb-1 mb-md-2 p-0 d-flex flex-column align-items-baseline">
              <input id="titleEntrada${cantidadEntradas}" type="text" maxlength="64" size="64" class="m-0 ink-font" value="${tituloEntrada}" placeholder="Título de la entrada...">
            </div>
            <div class="modal-body ms-2 ms-sm-3 ms-md-4 me-2 me-sm-3 me-md-4 mb-1 mb-md-2 p-0 d-flex flex-column align-items-baseline">
              <span class="ink-font m-0 unselectable me-1 me-md-2">Contenido: </span>
              <textarea class="w-100 m-0 shadow-none rounded-0 unselectable ink-font transparent-background" id="contenidoEntrada${cantidadEntradas}" rows="7" placeholder="Escribe aquí..."></textarea>
            </div>
            <div class="modal-footer ms-2 ms-sm-3 ms-md-4 me-2 me-sm-3 me-md-4 mb-1 mb-md-2 p-0 d-flex flex-column align-items-baseline">
              <a href="javascript:guardarEntrada(${cantidadEntradas});" class="btn btn-outline-light ms-0 me-0 mb-1 mb-md-2 mt-2 mt-md-3 roboto-font rounded-0 p-1 p-md-2 shadow-none w-100" aria-label="Close">Guardar entrada</a>
              <a href="javascript:eliminarEntrada(${cantidadEntradas});" class="btn btn-danger ms-0 me-0 mb-2 mb-md-3 roboto-font rounded-0 p-1 p-md-2 shadow-none w-100" aria-label="Close">Eliminar entrada</a>
            </div>
          </div>
        </div>
      </div>

      <input id="entradaID${cantidadEntradas}" type="hidden" value=""></input>
    `;

    $("#categoria0").append(tr);
    $("#entrada-input0").val('');
    var id_token = auth2.currentUser.get().getAuthResponse(true).id_token;
    $.ajax({
      url: '/diario/create',
      type: 'POST',
      data: JSON.stringify({
        token: id_token,
        titulo: tituloEntrada
      }),
      contentType: "application/json; charset=utf-8",
      traditional: true,
      success: function(data) {
        $(`#entradaID${cantidadEntradas}`).val(`${data}`)
      }
    })
    .done(function() {
      $("#cantidadEntradas").val((cantidadEntradas + 1).toString())
      diario = $("#main-content").outerHTML();
    });
    $.ajax({
      url: '/usuario/incrementar-xp',
      type: 'POST',
      data: JSON.stringify({
        token: id_token,
        xp: 10
      }),
      contentType: "application/json; charset=utf-8",
      traditional: true,
      success: function(data) {
        usuario[0][2] += 10;
        actualizarXP();
      }
    });
  }
});

const eliminarEntrada = async (entrada_id) => {
  $('.btn-close').click(); 
  document.getElementById('modalEntrada' + entrada_id).remove();
  document.getElementById('rowEntrada' + entrada_id).remove();
  var actualEntrada_id = $('#entradaID' + entrada_id).val();
  var id_token = auth2.currentUser.get().getAuthResponse(true).id_token
  $.ajax({
    url: '/diario/delete',
    type: 'DELETE',
    data: JSON.stringify({
      token: id_token,
      entrada_id: actualEntrada_id
    }),
    contentType: "application/json; charset=utf-8",
    traditional: true,
    success: function(data) {
      
    }
  });
  await delay(300);
  diario = $("#main-content").outerHTML();
}

const guardarEntrada = async (entrada_id) => {
  $('.btn-close').click(); 
  var actualEntrada_id = $('#entradaID' + entrada_id).val();
  var titulo = $("#titleEntrada" + entrada_id).val();
  var contenido = $("#contenidoEntrada" + entrada_id).val();
  var fechaActual = (new Date(Date.now()).toLocaleDateString()).toString() + " " + (new Date(Date.now()).toLocaleTimeString()).toString();
  var id_token = auth2.currentUser.get().getAuthResponse(true).id_token;
  var target = document.getElementById("rowEntrada" + entrada_id).getElementsByClassName("roboto-font")[0];
  target.innerHTML = fechaActual;
  target = document.getElementById("rowEntrada" + entrada_id).getElementsByClassName("ink-font")[0];
  target.innerHTML = titulo;
  $.ajax({
    url: '/diario',
    type: 'PUT',
    data: JSON.stringify({
      token: id_token,
      entrada_id: actualEntrada_id,
      titulo: titulo,
      contenido: contenido,
      fecha_actual: fechaActual
    }),
    contentType: "application/json; charset=utf-8",
    traditional: true,
    success: function(data) {
      
    }
  });
  $.ajax({
    url: '/usuario/incrementar-xp',
    type: 'POST',
    data: JSON.stringify({
      token: id_token,
      xp: 10
    }),
    contentType: "application/json; charset=utf-8",
    traditional: true,
    success: function(data) {
      usuario[0][2] += 10;
      actualizarXP();
    }
  });
  await delay(300);
  diario = $("#main-content").outerHTML();
}



var tiempoFaltante = 0;
var intervalo;
var vueltas = 0;

function startPomodoro() {
  var target = $(".tomato-img");
  target.removeClass("tomato-img");
  target.addClass("tomato-img-clicked");
  target.parent().attr('href', 'javascript:stopPomodoro();');
  tiempoFaltante = parseInt($("#duracionPomodoro").val()) * 1000 * 60;
  document.getElementById("pomodoroTitle").innerHTML = "Pomodoro";
  $("#pomodoroSelectorContainer").addClass("d-none");
  $("#pomodoroContainer").removeClass("d-none");
  //tiempoFin = Date.now() + tiempoFaltante
  if (vueltas < 3) {
    document.getElementById('pomodoroNext').innerHTML = 'Próximo: Descanso ' + timeToString(parseInt($("#duracionDescanso").val()) * 1000 * 60);
  } else if (vueltas == 3) {
    document.getElementById('pomodoroNext').innerHTML = 'Próximo: Descanso Largo ' + timeToString(parseInt($("#duracionDescansoLargo").val()) * 1000 * 60);
  }
  intervalo = setInterval(function printPomodoro() {
    tiempoFaltante = tiempoFaltante - 25
    try {
      document.getElementById("pomodoroTimerSpan").innerHTML = timeToString(tiempoFaltante);
      pomodoro = $("#main-content").outerHTML();
    } catch (error) {
      
    }

    if (tiempoFaltante <= 0 && vueltas < 4) {
      vueltas += 1;
      var id_token = auth2.currentUser.get().getAuthResponse(true).id_token
      $.ajax({
        url: '/usuario/incrementar-xp',
        type: 'POST',
        data: JSON.stringify({
          token: id_token,
          xp: 20
        }),
        contentType: "application/json; charset=utf-8",
        traditional: true,
        success: function(data) {
          usuario[0][2] += 20;
          actualizarXP();
        }
      });
      clearInterval(intervalo);
      tiempoFaltante = parseInt($("#duracionDescanso").val()) * 1000 * 60;
      document.getElementById('pomodoroNext').innerHTML = 'Próximo: Pomodoro ' + timeToString(parseInt($("#duracionPomodoro").val()) * 1000 * 60);
      document.getElementById("pomodoroTitle").innerHTML = "Descanso";
      intervalo = setInterval(function printPomodoro() {
        tiempoFaltante = tiempoFaltante - 25
        try {
          document.getElementById("pomodoroTimerSpan").innerHTML = timeToString(tiempoFaltante);
          pomodoro = $("#main-content").outerHTML();
        } catch (error) {
          
        }
        if (tiempoFaltante <= 0) {
          clearInterval(intervalo);
          startPomodoro();
        }
      }, 25);
    } else if (tiempoFaltante <= 0 && vueltas >= 4) {
      vueltas = 0;
      tiempoFaltante = parseInt($("#duracionDescansoLargo").val()) * 1000 * 60;
      clearInterval(intervalo);
      document.getElementById('pomodoroNext').innerHTML = 'Próximo: Pomodoro ' + timeToString(parseInt($("#duracionPomodoro").val()) * 1000 * 60);
      document.getElementById("pomodoroTitle").innerHTML = "Descanso Largo";
      intervalo = setInterval(function printPomodoro() {
        tiempoFaltante = tiempoFaltante - 25
        try {
          document.getElementById("pomodoroTimerSpan").innerHTML = timeToString(tiempoFaltante);
          pomodoro = $("#main-content").outerHTML();
        } catch (error) {
          
        }
        if (tiempoFaltante <= 0) {
          clearInterval(intervalo);
          startPomodoro();
        }
      }, 25);
    }
  }, 25);
}

function stopPomodoro() {
  $("#pomodoroSelectorContainer").removeClass("d-none");
  $("#pomodoroContainer").addClass("d-none");
  var target = $(".tomato-img-clicked");
  target.removeClass("tomato-img-clicked");
  target.addClass("tomato-img");
  target.parent().attr('href', 'javascript:startPomodoro();')

  clearInterval(intervalo);
  vueltas = 0;
  
}
