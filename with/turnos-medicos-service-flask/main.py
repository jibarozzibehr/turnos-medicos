import helper
from flask import Flask, request, Response, json, render_template
from flask_cors import CORS
import json
from flasgger import Swagger

app = Flask(__name__)
cors = CORS(app, resources={r"*": {"origins": "*"}})

app.config['SWAGGER'] = {
    'title': 'Events API',
    'version': '1.0.0',
    'description': '<h2>Turnos Médicos service\'s API.</h2> <h3>Asis, Butros <br> Barozzi Behr, Juan Ignacio <br> Oviedo, Lucas</h3> <br> LAB-IV - 2020.',
    
    # 'doc_dir': './examples/docs/'
}
swagger = Swagger(app)



#Agrega un nuevo turno a la db
@app.route('/events/new', methods=['POST'])
def add_event():
    """Adds a new event.
    Adds a new event and returns success or an error.
    ---
    tags:
      - events
    parameters:
      - name: event
        in: JSON
        type: object
        #enum: ['all', 'rgb', 'cmyk']
        required: true
        default: {"clinicID": 1, "professionalID": 2, "codClient": 76, "practiceID": 4, "reservationDate": "25-11-2020 12:00", "appointmentDay": "25-11-2020 12:00", "notified": 0, "cancelled": 0, "finalized": 0, "title": "Dolor de cabeza", "description": "Migraña"}
    definitions:
      Event:
        type: object
        properties:
          clinicID:
            type: integer
          professionalID:
            type: integer
          codClient:
            type: integer
          practiceID:
            type: integer
          reservationDate:
            type: string
          appointmentDay:
            type: string
          notified:
            type: integer
          cancelled:
            type: integer
          finalized:
            type: integer
          title:
            type: string
          description:
            type: string
      Response:
        type: object
        properties:
          error:
            type: integer
          status:
            type: string
      #Palette:
      #  type: object
      #  properties:
      #    palette_name:
      #      type: array
      #      items:
      #        $ref: '#/definitions/Color'
      #Color:
      #  type: string
    responses:
      200:
        description: The error code and status.
        schema:
          $ref: '#/definitions/Response'
        examples:
          {"error": 0, "status": 'Success'}
          #{"clinicID": 1, "professionalID": 2, "codClient": 76, "practiceID": 4, "reservationDate": "25-11-2020 12:00", "appointmentDay": "25-11-2020 12:00", "notified": 0, "cancelled": 0, "finalized": 0, "title": "Dolor de cabeza", "description": "Migraña"}
    """
    req_data = request.get_json()

    clinicID = req_data['clinicID']
    professionalID = req_data['professionalID']
    codClient = req_data['codClient']
    practiceID = req_data['practiceID']
    reservationDate = req_data['reservationDate']
    appointmentDay = req_data['appointmentDay']
    notified = req_data['notified']
    cancelled = req_data['cancelled']
    finalized = req_data['finalized']
    
    title = req_data['title']
    description = req_data['description']

    data = [clinicID,professionalID,codClient,practiceID,reservationDate,appointmentDay,notified,cancelled,finalized,title,description]
    

    # Add item to the list
    res_data = helper.add_event(data)

    # Return error if item not added
    if res_data is None:
        response = Response("{'error': 'Event not added - " + title + "'}", status=500 , mimetype='application/json')
        return response

    # Return response
    response = Response(json.dumps(res_data), mimetype='application/json')

    return response

#Modifica un turno de la db
@app.route('/events/update', methods=['PUT'])
def update_event():
    """Updates an event.
    Updates an existing event and returns success or an error with a status.
    ---
    tags:
      - events
    parameters:
      - name: event
        in: JSON
        type: object
        #enum: ['all', 'rgb', 'cmyk']
        required: true
        default: {"clinicID": 1, "professionalID": 2, "codClient": 76, "practiceID": 4, "reservationDate": "25-11-2020 12:00", "appointmentDay": "25-11-2020 12:00", "notified": 0, "cancelled": 0, "finalized": 0, "title": "Dolor de cabeza", "description": "Migraña"}
    definitions:
      Event:
        type: object
        properties:
          clinicID:
            type: integer
          professionalID:
            type: integer
          codClient:
            type: integer
          practiceID:
            type: integer
          reservationDate:
            type: string
          appointmentDay:
            type: string
          notified:
            type: integer
          cancelled:
            type: integer
          finalized:
            type: integer
          title:
            type: string
          description:
            type: string
      Response:
        type: object
        properties:
          error:
            type: integer
          status:
            type: string
      #Palette:
      #  type: object
      #  properties:
      #    palette_name:
      #      type: array
      #      items:
      #        $ref: '#/definitions/Color'
      #Color:
      #  type: string
    responses:
      200:
        description: The error code and status. An error code of "0" means success.
        schema:
          $ref: '#/definitions/Response'
        examples:
          {"error": 0, "status": 'Success'}
          #{"clinicID": 1, "professionalID": 2, "codClient": 76, "practiceID": 4, "reservationDate": "25-11-2020 12:00", "appointmentDay": "25-11-2020 12:00", "notified": 0, "cancelled": 0, "finalized": 0, "title": "Dolor de cabeza", "description": "Migraña"}
    """
    req_data = request.get_json()
    appointmentID = req_data['appointmentID']
    clinicID = req_data['clinicID']
    professionalID = req_data['professionalID']
    codClient = req_data['codClient']
    practiceID = req_data['practiceID']
    reservationDate = req_data['reservationDate']
    appointmentDay = req_data['appointmentDay']
    notified = req_data['notified']
    cancelled = req_data['cancelled']
    finalized = req_data['finalized']
    
    title = req_data['title']
    description = req_data['description']

    data = [appointmentID, clinicID,professionalID,codClient,practiceID,reservationDate,appointmentDay,notified,cancelled,finalized,title,description]
    

    # Add item to the list
    res_data = helper.update_event(data)

    # Return error if item not added
    if res_data is None:
        response = Response("{'error': 'Event not modified - " + title + "'}", status=500 , mimetype='application/json')
        return response

    # Return response
    response = Response(json.dumps(res_data), mimetype='application/json')

    return response

#Modifica un turno de la db (elimina)
@app.route('/events/deleteEvent', methods=['PUT'])
def delete_event():
    """Deletes an event.
    Deletes an event changing the value of "cancelled" to "1".
    ---
    tags:
      - events
    parameters:
      - name: appointment
        in: JSON
        type: object
        #enum: ['all', 'rgb', 'cmyk']
        required: true
        default: {"appointmentID": 345}
    definitions:
      Appointment:
        type: object
        properties:
          appointmentID:
            type: integer
      Response:
        type: object
        properties:
          error:
            type: integer
          status:
            type: string
      #Palette:
      #  type: object
      #  properties:
      #    palette_name:
      #      type: array
      #      items:
      #        $ref: '#/definitions/Color'
      #Color:
      #  type: string
    responses:
      200:
        description: The error code and status. An error code of "0" means success.
        schema:
          $ref: '#/definitions/Response'
        examples:
          {"error": 0, "status": 'Success'}
          #{"clinicID": 1, "professionalID": 2, "codClient": 76, "practiceID": 4, "reservationDate": "25-11-2020 12:00", "appointmentDay": "25-11-2020 12:00", "notified": 0, "cancelled": 0, "finalized": 0, "title": "Dolor de cabeza", "description": "Migraña"}
    """
    req_data = request.get_json()
    appointmentID = req_data['appointmentID']

    data = [appointmentID]

    

    # Add item to the list
    res_data = helper.delete_event(data)

    # Return error if item not added
    if res_data is None:
        response = Response("{'error': 'Event not modified - ID: " + appointmentID + "'}", status=500 , mimetype='application/json')
        return response

    # Return response
    response = Response(json.dumps(res_data), mimetype='application/json')

    return response

#Modifica un turno de la db (notifica)
@app.route('/events/notifyEvent', methods=['PUT'])
def notify_event():
    """Notifies about an upcoming event.
    Notifies about an upcoming event and marks it as "notified".
    ---
    tags:
      - events
    parameters:
      - name: appointment
        in: JSON
        type: object
        #enum: ['all', 'rgb', 'cmyk']
        required: true
        default: {"appointmentID": 345}
    definitions:
      Appointment:
        type: object
        properties:
          appointmentID:
            type: integer
      Response:
        type: object
        properties:
          error:
            type: integer
          status:
            type: string
      #Palette:
      #  type: object
      #  properties:
      #    palette_name:
      #      type: array
      #      items:
      #        $ref: '#/definitions/Color'
      #Color:
      #  type: string
    responses:
      200:
        description: The error code and status. An error code of "0" means success.
        schema:
          $ref: '#/definitions/Response'
        examples:
          {"error": 0, "status": 'Success'}
          #{"clinicID": 1, "professionalID": 2, "codClient": 76, "practiceID": 4, "reservationDate": "25-11-2020 12:00", "appointmentDay": "25-11-2020 12:00", "notified": 0, "cancelled": 0, "finalized": 0, "title": "Dolor de cabeza", "description": "Migraña"}
    """
    req_data = request.get_json()
    appointmentID = req_data['appointmentID']

    data = [appointmentID]
    

    # Add item to the list
    res_data = helper.notify_event(data)

    # Return error if item not added
    if res_data is None:
        response = Response("{'error': 'Event not modified - ID: " + appointmentID + "'}", status=500 , mimetype='application/json')
        return response

    # Return response
    response = Response(json.dumps(res_data), mimetype='application/json')

    return response

#Modifica un turno de la db (finaliza)
@app.route('/events/finalizeEvent', methods=['PUT'])
def finalize_event():
    """Finalizes an event.
    Finalizes an event marking it as "finalized".
    ---
    tags:
      - events
    parameters:
      - name: appointment
        in: JSON
        type: object
        #enum: ['all', 'rgb', 'cmyk']
        required: true
        default: {"appointmentID": 345}
    definitions:
      Appointment:
        type: object
        properties:
          appointmentID:
            type: integer
      Response:
        type: object
        properties:
          error:
            type: integer
          status:
            type: string
      #Palette:
      #  type: object
      #  properties:
      #    palette_name:
      #      type: array
      #      items:
      #        $ref: '#/definitions/Color'
      #Color:
      #  type: string
    responses:
      200:
        description: The error code and status. An error code of "0" means success.
        schema:
          $ref: '#/definitions/Response'
        examples:
          {"error": 0, "status": 'Success'}
          #{"clinicID": 1, "professionalID": 2, "codClient": 76, "practiceID": 4, "reservationDate": "25-11-2020 12:00", "appointmentDay": "25-11-2020 12:00", "notified": 0, "cancelled": 0, "finalized": 0, "title": "Dolor de cabeza", "description": "Migraña"}
    """
    req_data = request.get_json()
    appointmentID = req_data['appointmentID']

    data = [appointmentID]
    

    # Add item to the list
    res_data = helper.finalize_event(data)

    # Return error if item not added
    if res_data is None:
        response = Response("{'error': 'Event not modified - ID: " + appointmentID + "'}", status=500 , mimetype='application/json')
        return response

    # Return response
    response = Response(json.dumps(res_data), mimetype='application/json')

    return response





#Obtiene todos los turnos de un cliente
@app.route('/events/getClientEvents', methods=['GET'])
def get_client_events():
    """Gets all the events for a specified client.
    Gets all the events for a specified client.
    ---
    tags:
      - events
    parameters:
      - name: clientID
        in: query
        type: integer
        #enum: ['all', 'rgb', 'cmyk']
        required: true
        #default: 0
        description: Client's ID.
    definitions:
      Event:
        type: object
        properties:
          ID:
            type: integer
          Clinica_ID:
            type: integer
          Profesional_Matricula:
            type: integer
          Cod_Paciente:
            type: integer
          Practica_ID:
            type: integer
          Fecha_Reserva:
            type: string
          Fecha_Turno:
            type: string
          Notificado:
            type: integer
          Cancelado:
            type: integer
          Finalizado:
            type: string
          Titulo:
            type: string
          Descripcion:
            type: string
      Events:
        type: object
        properties:
          error:
            type: integer
          status:
            type: array
            items:
              $ref: '#/definitions/Event'
      #Palette:
      #  type: object
      #  properties:
      #    palette_name:
      #      type: array
      #      items:
      #        $ref: '#/definitions/Color'
      #Color:
      #  type: string
    responses:
      200:
        description: The error code and status. An error code of "0" means success.
        schema:
          $ref: '#/definitions/Events'
        examples:
          #{"error": 0, "status": 'Success'}
          {"error": 0, "status": [{"ID": 1, "Clinica_ID": 1, "Profesional_Matricula": 123456, "Cod_Paciente": 1, "Practica_ID": 1, "Fecha_Reserva": "11-11-2020 18:48", "Fecha_Turno": "2020-11-24 12:00", "Notificado": 0, "Cancelado": 1, "Finalizado": 0, "Titulo": "Limprieza para los dientes", "Descripcion": "Estan muy sucios"}, {"ID": 2, "Clinica_ID": 1, "Profesional_Matricula": 1, "Cod_Paciente": 1, "Practica_ID": 3, "Fecha_Reserva": "2020-11-11", "Fecha_Turno": "2020-11-26 20:34", "Notificado": 0, "Cancelado": 0, "Finalizado": 0, "Titulo": "Consulta con Dios", "Descripcion": "Solo Dios sabe"}, {"ID": 3, "Clinica_ID": 1, "Profesional_Matricula": 123456, "Cod_Paciente": 1, "Practica_ID": 1, "Fecha_Reserva": "25-11-2020 12:00", "Fecha_Turno": "2020-11-25 13:00", "Notificado": 0, "Cancelado": 0, "Finalizado": 0, "Titulo": "Esto es una prueba", "Descripcion": "Prueba UPDATE"}, {"ID": 4, "Clinica_ID": 1, "Profesional_Matricula": 123456, "Cod_Paciente": 1, "Practica_ID": 1, "Fecha_Reserva": "25-11-2020 11:00", "Fecha_Turno": "2020-11-25 14:00", "Notificado": 0, "Cancelado": 0, "Finalizado": 0, "Titulo": "Esto es una prueba222", "Descripcion": "Pruebaaaaa"}, {"ID": 5, "Clinica_ID": 1, "Profesional_Matricula": 123456, "Cod_Paciente": 1, "Practica_ID": 1, "Fecha_Reserva": "25-11-2020 12:00", "Fecha_Turno": "2020-11-19 18:00", "Notificado": 0, "Cancelado": 0, "Finalizado": 0, "Titulo": "Esto es una prueba", "Descripcion": "Prueba consulta"}, {"ID": 6, "Clinica_ID": 3, "Profesional_Matricula": 1, "Cod_Paciente": 1, "Practica_ID": 3, "Fecha_Reserva": "2020-11-26 20:00", "Fecha_Turno": "2020-11-27 21:00", "Notificado": 0, "Cancelado": 0, "Finalizado": 0, "Titulo": "Este es el t\u00edtulo.", "Descripcion": "Esta es la descripci\u00f3n."}, {"ID": 7, "Clinica_ID": 1, "Profesional_Matricula": 1, "Cod_Paciente": 1, "Practica_ID": 3, "Fecha_Reserva": "2020-11-27 14:54", "Fecha_Turno": "2020-11-30 12:00", "Notificado": 0, "Cancelado": 1, "Finalizado": 0, "Titulo": "Razon", "Descripcion": "Esta todo mal"}, {"ID": 8, "Clinica_ID": 1, "Profesional_Matricula": 1, "Cod_Paciente": 1, "Practica_ID": 3, "Fecha_Reserva": "2020-11-27 14:59", "Fecha_Turno": "2020-11-30 13:00", "Notificado": 0, "Cancelado": 1, "Finalizado": 0, "Titulo": "mallllll", "Descripcion": "Malisimo"}, {"ID": 9, "Clinica_ID": 1, "Profesional_Matricula": 1, "Cod_Paciente": 1, "Practica_ID": 3, "Fecha_Reserva": "2020-11-27 15:02", "Fecha_Turno": "2020-11-30 17:00", "Notificado": 0, "Cancelado": 1, "Finalizado": 0, "Titulo": "Esta m,al", "Descripcion": "asndasd"}, {"ID": 10, "Clinica_ID": 1, "Profesional_Matricula": 1, "Cod_Paciente": 1, "Practica_ID": 3, "Fecha_Reserva": "2020-11-27 15:06", "Fecha_Turno": "2020-11-30 15:00", "Notificado": 0, "Cancelado": 1, "Finalizado": 0, "Titulo": "asdjkl", "Descripcion": "asjdkl"}, {"ID": 11, "Clinica_ID": 1, "Profesional_Matricula": 1, "Cod_Paciente": 1, "Practica_ID": 3, "Fecha_Reserva": "2020-11-27 15:13", "Fecha_Turno": "2020-11-30 18:00", "Notificado": 0, "Cancelado": 1, "Finalizado": 0, "Titulo": "asddas", "Descripcion": "dddddddddddddddd"}, {"ID": 12, "Clinica_ID": 1, "Profesional_Matricula": 1, "Cod_Paciente": 1, "Practica_ID": 3, "Fecha_Reserva": "2020-11-27 15:28", "Fecha_Turno": "2020-11-30 11:00", "Notificado": 0, "Cancelado": 0, "Finalizado": 0, "Titulo": "Pruebaaaaa", "Descripcion": "234423234234"}, {"ID": 13, "Clinica_ID": 1, "Profesional_Matricula": 1, "Cod_Paciente": 1, "Practica_ID": 3, "Fecha_Reserva": "2020-11-27 15:35", "Fecha_Turno": "2020-12-02 11:00", "Notificado": 0, "Cancelado": 1, "Finalizado": 0, "Titulo": "Dolor de cabeza", "Descripcion": "Me duele la cabeza."}, {"ID": 15, "Clinica_ID": 1, "Profesional_Matricula": 1, "Cod_Paciente": 1, "Practica_ID": 3, "Fecha_Reserva": "2020-11-27 17:36", "Fecha_Turno": "2020-12-04 15:00", "Notificado": 0, "Cancelado": 1, "Finalizado": 0, "Titulo": "Dolor de cabeza", "Descripcion": "Me duele la cabeza."}, {"ID": 22, "Clinica_ID": 1, "Profesional_Matricula": 1, "Cod_Paciente": 1, "Practica_ID": 3, "Fecha_Reserva": "2020-12-19 12:27", "Fecha_Turno": "2020-12-22 13:00", "Notificado": 0, "Cancelado": 0, "Finalizado": 1, "Titulo": "2", "Descripcion": ""}, {"ID": 23, "Clinica_ID": 1, "Profesional_Matricula": 1, "Cod_Paciente": 1, "Practica_ID": 3, "Fecha_Reserva": "2020-12-19 12:27", "Fecha_Turno": "2020-12-22 14:00", "Notificado": 0, "Cancelado": 0, "Finalizado": 1, "Titulo": "3", "Descripcion": ""}, {"ID": 24, "Clinica_ID": 1, "Profesional_Matricula": 1, "Cod_Paciente": 1, "Practica_ID": 3, "Fecha_Reserva": "2020-12-19 12:27", "Fecha_Turno": "2020-12-22 15:00", "Notificado": 0, "Cancelado": 0, "Finalizado": 1, "Titulo": "4", "Descripcion": ""}, {"ID": 25, "Clinica_ID": 1, "Profesional_Matricula": 1, "Cod_Paciente": 1, "Practica_ID": 3, "Fecha_Reserva": "2020-12-19 12:27", "Fecha_Turno": "2020-12-22 17:00", "Notificado": 0, "Cancelado": 0, "Finalizado": 1, "Titulo": "45", "Descripcion": ""}, {"ID": 26, "Clinica_ID": 1, "Profesional_Matricula": 1, "Cod_Paciente": 1, "Practica_ID": 3, "Fecha_Reserva": "2020-12-19 12:28", "Fecha_Turno": "2020-12-22 18:00", "Notificado": 0, "Cancelado": 0, "Finalizado": 1, "Titulo": "33", "Descripcion": ""}, {"ID": 27, "Clinica_ID": 1, "Profesional_Matricula": 1, "Cod_Paciente": 1, "Practica_ID": 3, "Fecha_Reserva": "2020-12-19 12:28", "Fecha_Turno": "2020-12-22 19:00", "Notificado": 0, "Cancelado": 0, "Finalizado": 1, "Titulo": "23234234", "Descripcion": "323234"}, {"ID": 28, "Clinica_ID": 1, "Profesional_Matricula": 1, "Cod_Paciente": 1, "Practica_ID": 3, "Fecha_Reserva": "2020-12-19 16:57", "Fecha_Turno": "2020-12-22 15:00", "Notificado": 0, "Cancelado": 0, "Finalizado": 0, "Titulo": "Se siente mal", "Descripcion": "Anda mal."}]}
          #{"clinicID": 1, "professionalID": 2, "codClient": 76, "practiceID": 4, "reservationDate": "25-11-2020 12:00", "appointmentDay": "25-11-2020 12:00", "notified": 0, "cancelled": 0, "finalized": 0, "title": "Dolor de cabeza", "description": "Migraña"}
    """
    clientID = request.args.get('clientID')

    # Get items from the helper
    status = helper.get_client_events(clientID)

    # Return 404 if item not found
    if status is None:
        respuesta = {"error":"Client not found (clientID=" + str(clientID) + ")."}
        response = Response(json.dumps(respuesta), status=404 , mimetype='application/json')
        return response

    # Return status
    """res_data = {
        'status': status
    }"""

    response = Response(json.dumps(status), status=200, mimetype='application/json')
    return response



#Obtiene todos los turnos de un profesional.
@app.route('/events/getProfessionalEvents', methods=['GET'])
def get_professional_events():
    """Gets all the events for a specified professional.
    Gets all the events for a specified professional.
    ---
    tags:
      - events
    parameters:
      - name: professionalID
        in: query
        type: integer
        #enum: ['all', 'rgb', 'cmyk']
        required: true
        #default: {"professionalID": 456}
        description: Professional's ID.
    definitions:
      Event:
        type: object
        properties:
          ID:
            type: integer
          Clinica_ID:
            type: integer
          Profesional_Matricula:
            type: integer
          Cod_Paciente:
            type: integer
          Practica_ID:
            type: integer
          Fecha_Reserva:
            type: string
          Fecha_Turno:
            type: string
          Notificado:
            type: integer
          Cancelado:
            type: integer
          Finalizado:
            type: string
          Titulo:
            type: string
          Descripcion:
            type: string
      Events:
        type: object
        properties:
          error:
            type: integer
          status:
            type: array
            items:
              $ref: '#/definitions/Event'
      #Palette:
      #  type: object
      #  properties:
      #    palette_name:
      #      type: array
      #      items:
      #        $ref: '#/definitions/Color'
      #Color:
      #  type: string
    responses:
      200:
        description: The error code and status. An error code of "0" means success.
        schema:
          $ref: '#/definitions/Events'
        examples:
          #{"error": 0, "status": 'Success'}
          {"error": 0, "status": [{"ID": 1, "Clinica_ID": 1, "Profesional_Matricula": 123456, "Cod_Paciente": 1, "Practica_ID": 1, "Fecha_Reserva": "11-11-2020 18:48", "Fecha_Turno": "2020-11-24 12:00", "Notificado": 0, "Cancelado": 1, "Finalizado": 0, "Titulo": "Limprieza para los dientes", "Descripcion": "Estan muy sucios"}, {"ID": 2, "Clinica_ID": 1, "Profesional_Matricula": 1, "Cod_Paciente": 1, "Practica_ID": 3, "Fecha_Reserva": "2020-11-11", "Fecha_Turno": "2020-11-26 20:34", "Notificado": 0, "Cancelado": 0, "Finalizado": 0, "Titulo": "Consulta con Dios", "Descripcion": "Solo Dios sabe"}, {"ID": 3, "Clinica_ID": 1, "Profesional_Matricula": 123456, "Cod_Paciente": 1, "Practica_ID": 1, "Fecha_Reserva": "25-11-2020 12:00", "Fecha_Turno": "2020-11-25 13:00", "Notificado": 0, "Cancelado": 0, "Finalizado": 0, "Titulo": "Esto es una prueba", "Descripcion": "Prueba UPDATE"}, {"ID": 4, "Clinica_ID": 1, "Profesional_Matricula": 123456, "Cod_Paciente": 1, "Practica_ID": 1, "Fecha_Reserva": "25-11-2020 11:00", "Fecha_Turno": "2020-11-25 14:00", "Notificado": 0, "Cancelado": 0, "Finalizado": 0, "Titulo": "Esto es una prueba222", "Descripcion": "Pruebaaaaa"}, {"ID": 5, "Clinica_ID": 1, "Profesional_Matricula": 123456, "Cod_Paciente": 1, "Practica_ID": 1, "Fecha_Reserva": "25-11-2020 12:00", "Fecha_Turno": "2020-11-19 18:00", "Notificado": 0, "Cancelado": 0, "Finalizado": 0, "Titulo": "Esto es una prueba", "Descripcion": "Prueba consulta"}, {"ID": 6, "Clinica_ID": 3, "Profesional_Matricula": 1, "Cod_Paciente": 1, "Practica_ID": 3, "Fecha_Reserva": "2020-11-26 20:00", "Fecha_Turno": "2020-11-27 21:00", "Notificado": 0, "Cancelado": 0, "Finalizado": 0, "Titulo": "Este es el t\u00edtulo.", "Descripcion": "Esta es la descripci\u00f3n."}, {"ID": 7, "Clinica_ID": 1, "Profesional_Matricula": 1, "Cod_Paciente": 1, "Practica_ID": 3, "Fecha_Reserva": "2020-11-27 14:54", "Fecha_Turno": "2020-11-30 12:00", "Notificado": 0, "Cancelado": 1, "Finalizado": 0, "Titulo": "Razon", "Descripcion": "Esta todo mal"}, {"ID": 8, "Clinica_ID": 1, "Profesional_Matricula": 1, "Cod_Paciente": 1, "Practica_ID": 3, "Fecha_Reserva": "2020-11-27 14:59", "Fecha_Turno": "2020-11-30 13:00", "Notificado": 0, "Cancelado": 1, "Finalizado": 0, "Titulo": "mallllll", "Descripcion": "Malisimo"}, {"ID": 9, "Clinica_ID": 1, "Profesional_Matricula": 1, "Cod_Paciente": 1, "Practica_ID": 3, "Fecha_Reserva": "2020-11-27 15:02", "Fecha_Turno": "2020-11-30 17:00", "Notificado": 0, "Cancelado": 1, "Finalizado": 0, "Titulo": "Esta m,al", "Descripcion": "asndasd"}, {"ID": 10, "Clinica_ID": 1, "Profesional_Matricula": 1, "Cod_Paciente": 1, "Practica_ID": 3, "Fecha_Reserva": "2020-11-27 15:06", "Fecha_Turno": "2020-11-30 15:00", "Notificado": 0, "Cancelado": 1, "Finalizado": 0, "Titulo": "asdjkl", "Descripcion": "asjdkl"}, {"ID": 11, "Clinica_ID": 1, "Profesional_Matricula": 1, "Cod_Paciente": 1, "Practica_ID": 3, "Fecha_Reserva": "2020-11-27 15:13", "Fecha_Turno": "2020-11-30 18:00", "Notificado": 0, "Cancelado": 1, "Finalizado": 0, "Titulo": "asddas", "Descripcion": "dddddddddddddddd"}, {"ID": 12, "Clinica_ID": 1, "Profesional_Matricula": 1, "Cod_Paciente": 1, "Practica_ID": 3, "Fecha_Reserva": "2020-11-27 15:28", "Fecha_Turno": "2020-11-30 11:00", "Notificado": 0, "Cancelado": 0, "Finalizado": 0, "Titulo": "Pruebaaaaa", "Descripcion": "234423234234"}, {"ID": 13, "Clinica_ID": 1, "Profesional_Matricula": 1, "Cod_Paciente": 1, "Practica_ID": 3, "Fecha_Reserva": "2020-11-27 15:35", "Fecha_Turno": "2020-12-02 11:00", "Notificado": 0, "Cancelado": 1, "Finalizado": 0, "Titulo": "Dolor de cabeza", "Descripcion": "Me duele la cabeza."}, {"ID": 15, "Clinica_ID": 1, "Profesional_Matricula": 1, "Cod_Paciente": 1, "Practica_ID": 3, "Fecha_Reserva": "2020-11-27 17:36", "Fecha_Turno": "2020-12-04 15:00", "Notificado": 0, "Cancelado": 1, "Finalizado": 0, "Titulo": "Dolor de cabeza", "Descripcion": "Me duele la cabeza."}, {"ID": 22, "Clinica_ID": 1, "Profesional_Matricula": 1, "Cod_Paciente": 1, "Practica_ID": 3, "Fecha_Reserva": "2020-12-19 12:27", "Fecha_Turno": "2020-12-22 13:00", "Notificado": 0, "Cancelado": 0, "Finalizado": 1, "Titulo": "2", "Descripcion": ""}, {"ID": 23, "Clinica_ID": 1, "Profesional_Matricula": 1, "Cod_Paciente": 1, "Practica_ID": 3, "Fecha_Reserva": "2020-12-19 12:27", "Fecha_Turno": "2020-12-22 14:00", "Notificado": 0, "Cancelado": 0, "Finalizado": 1, "Titulo": "3", "Descripcion": ""}, {"ID": 24, "Clinica_ID": 1, "Profesional_Matricula": 1, "Cod_Paciente": 1, "Practica_ID": 3, "Fecha_Reserva": "2020-12-19 12:27", "Fecha_Turno": "2020-12-22 15:00", "Notificado": 0, "Cancelado": 0, "Finalizado": 1, "Titulo": "4", "Descripcion": ""}, {"ID": 25, "Clinica_ID": 1, "Profesional_Matricula": 1, "Cod_Paciente": 1, "Practica_ID": 3, "Fecha_Reserva": "2020-12-19 12:27", "Fecha_Turno": "2020-12-22 17:00", "Notificado": 0, "Cancelado": 0, "Finalizado": 1, "Titulo": "45", "Descripcion": ""}, {"ID": 26, "Clinica_ID": 1, "Profesional_Matricula": 1, "Cod_Paciente": 1, "Practica_ID": 3, "Fecha_Reserva": "2020-12-19 12:28", "Fecha_Turno": "2020-12-22 18:00", "Notificado": 0, "Cancelado": 0, "Finalizado": 1, "Titulo": "33", "Descripcion": ""}, {"ID": 27, "Clinica_ID": 1, "Profesional_Matricula": 1, "Cod_Paciente": 1, "Practica_ID": 3, "Fecha_Reserva": "2020-12-19 12:28", "Fecha_Turno": "2020-12-22 19:00", "Notificado": 0, "Cancelado": 0, "Finalizado": 1, "Titulo": "23234234", "Descripcion": "323234"}, {"ID": 28, "Clinica_ID": 1, "Profesional_Matricula": 1, "Cod_Paciente": 1, "Practica_ID": 3, "Fecha_Reserva": "2020-12-19 16:57", "Fecha_Turno": "2020-12-22 15:00", "Notificado": 0, "Cancelado": 0, "Finalizado": 0, "Titulo": "Se siente mal", "Descripcion": "Anda mal."}]}
          #{"clinicID": 1, "professionalID": 2, "codClient": 76, "practiceID": 4, "reservationDate": "25-11-2020 12:00", "appointmentDay": "25-11-2020 12:00", "notified": 0, "cancelled": 0, "finalized": 0, "title": "Dolor de cabeza", "description": "Migraña"}
    """
    professionalID = request.args.get('professionalID')


    # Get items from the helper
    status = helper.get_professional_events(professionalID)

    # Return 404 if item not found
    if status is None:
        respuesta = {"error":"Professional not found (professionalID = " + str(professionalID) + ")."}
        response = Response(json.dumps(respuesta), status=404 , mimetype='application/json')
        return response

    # Return status
    """res_data = {
        'status': status
    }"""

    response = Response(json.dumps(status), status=200, mimetype='application/json')
    return response



#Obtiene todos los turnos de un profesional en una clinica
@app.route('/events/getProfessionalEventsByClinic', methods=['GET'])
def get_professional_events_byClinic():
    """Gets all the events for a specified professional in a specific clinic.
    Gets all the events for a specified professional in a specific clinic.
    ---
    tags:
      - events
    parameters:
      - name: professionalID
        in: query
        type: integer
        #enum: ['all', 'rgb', 'cmyk']
        required: true
        #default: 1
        description: Professional's ID.
      - name: clinicID
        in: query
        type: integer
        #enum: ['all', 'rgb', 'cmyk']
        required: true
        #default: 3
        description: Clinic's ID.
    definitions:
      Event:
        type: object
        properties:
          ID:
            type: integer
          Clinica_ID:
            type: integer
          Profesional_Matricula:
            type: integer
          Cod_Paciente:
            type: integer
          Practica_ID:
            type: integer
          Fecha_Reserva:
            type: string
          Fecha_Turno:
            type: string
          Notificado:
            type: integer
          Cancelado:
            type: integer
          Finalizado:
            type: string
          Titulo:
            type: string
          Descripcion:
            type: string
      Events:
        type: object
        properties:
          error:
            type: integer
          status:
            type: array
            items:
              $ref: '#/definitions/Event'
      #Palette:
      #  type: object
      #  properties:
      #    palette_name:
      #      type: array
      #      items:
      #        $ref: '#/definitions/Color'
      #Color:
      #  type: string
    responses:
      200:
        description: The error code and status. An error code of "0" means success.
        schema:
          $ref: '#/definitions/Events'
        examples:
          #{"error": 0, "status": 'Success'}
          {"error": 0, "status": [{"ID": 1, "Clinica_ID": 1, "Profesional_Matricula": 123456, "Cod_Paciente": 1, "Practica_ID": 1, "Fecha_Reserva": "11-11-2020 18:48", "Fecha_Turno": "2020-11-24 12:00", "Notificado": 0, "Cancelado": 1, "Finalizado": 0, "Titulo": "Limprieza para los dientes", "Descripcion": "Estan muy sucios"}, {"ID": 2, "Clinica_ID": 1, "Profesional_Matricula": 1, "Cod_Paciente": 1, "Practica_ID": 3, "Fecha_Reserva": "2020-11-11", "Fecha_Turno": "2020-11-26 20:34", "Notificado": 0, "Cancelado": 0, "Finalizado": 0, "Titulo": "Consulta con Dios", "Descripcion": "Solo Dios sabe"}, {"ID": 3, "Clinica_ID": 1, "Profesional_Matricula": 123456, "Cod_Paciente": 1, "Practica_ID": 1, "Fecha_Reserva": "25-11-2020 12:00", "Fecha_Turno": "2020-11-25 13:00", "Notificado": 0, "Cancelado": 0, "Finalizado": 0, "Titulo": "Esto es una prueba", "Descripcion": "Prueba UPDATE"}, {"ID": 4, "Clinica_ID": 1, "Profesional_Matricula": 123456, "Cod_Paciente": 1, "Practica_ID": 1, "Fecha_Reserva": "25-11-2020 11:00", "Fecha_Turno": "2020-11-25 14:00", "Notificado": 0, "Cancelado": 0, "Finalizado": 0, "Titulo": "Esto es una prueba222", "Descripcion": "Pruebaaaaa"}, {"ID": 5, "Clinica_ID": 1, "Profesional_Matricula": 123456, "Cod_Paciente": 1, "Practica_ID": 1, "Fecha_Reserva": "25-11-2020 12:00", "Fecha_Turno": "2020-11-19 18:00", "Notificado": 0, "Cancelado": 0, "Finalizado": 0, "Titulo": "Esto es una prueba", "Descripcion": "Prueba consulta"}, {"ID": 6, "Clinica_ID": 3, "Profesional_Matricula": 1, "Cod_Paciente": 1, "Practica_ID": 3, "Fecha_Reserva": "2020-11-26 20:00", "Fecha_Turno": "2020-11-27 21:00", "Notificado": 0, "Cancelado": 0, "Finalizado": 0, "Titulo": "Este es el t\u00edtulo.", "Descripcion": "Esta es la descripci\u00f3n."}, {"ID": 7, "Clinica_ID": 1, "Profesional_Matricula": 1, "Cod_Paciente": 1, "Practica_ID": 3, "Fecha_Reserva": "2020-11-27 14:54", "Fecha_Turno": "2020-11-30 12:00", "Notificado": 0, "Cancelado": 1, "Finalizado": 0, "Titulo": "Razon", "Descripcion": "Esta todo mal"}, {"ID": 8, "Clinica_ID": 1, "Profesional_Matricula": 1, "Cod_Paciente": 1, "Practica_ID": 3, "Fecha_Reserva": "2020-11-27 14:59", "Fecha_Turno": "2020-11-30 13:00", "Notificado": 0, "Cancelado": 1, "Finalizado": 0, "Titulo": "mallllll", "Descripcion": "Malisimo"}, {"ID": 9, "Clinica_ID": 1, "Profesional_Matricula": 1, "Cod_Paciente": 1, "Practica_ID": 3, "Fecha_Reserva": "2020-11-27 15:02", "Fecha_Turno": "2020-11-30 17:00", "Notificado": 0, "Cancelado": 1, "Finalizado": 0, "Titulo": "Esta m,al", "Descripcion": "asndasd"}, {"ID": 10, "Clinica_ID": 1, "Profesional_Matricula": 1, "Cod_Paciente": 1, "Practica_ID": 3, "Fecha_Reserva": "2020-11-27 15:06", "Fecha_Turno": "2020-11-30 15:00", "Notificado": 0, "Cancelado": 1, "Finalizado": 0, "Titulo": "asdjkl", "Descripcion": "asjdkl"}, {"ID": 11, "Clinica_ID": 1, "Profesional_Matricula": 1, "Cod_Paciente": 1, "Practica_ID": 3, "Fecha_Reserva": "2020-11-27 15:13", "Fecha_Turno": "2020-11-30 18:00", "Notificado": 0, "Cancelado": 1, "Finalizado": 0, "Titulo": "asddas", "Descripcion": "dddddddddddddddd"}, {"ID": 12, "Clinica_ID": 1, "Profesional_Matricula": 1, "Cod_Paciente": 1, "Practica_ID": 3, "Fecha_Reserva": "2020-11-27 15:28", "Fecha_Turno": "2020-11-30 11:00", "Notificado": 0, "Cancelado": 0, "Finalizado": 0, "Titulo": "Pruebaaaaa", "Descripcion": "234423234234"}, {"ID": 13, "Clinica_ID": 1, "Profesional_Matricula": 1, "Cod_Paciente": 1, "Practica_ID": 3, "Fecha_Reserva": "2020-11-27 15:35", "Fecha_Turno": "2020-12-02 11:00", "Notificado": 0, "Cancelado": 1, "Finalizado": 0, "Titulo": "Dolor de cabeza", "Descripcion": "Me duele la cabeza."}, {"ID": 15, "Clinica_ID": 1, "Profesional_Matricula": 1, "Cod_Paciente": 1, "Practica_ID": 3, "Fecha_Reserva": "2020-11-27 17:36", "Fecha_Turno": "2020-12-04 15:00", "Notificado": 0, "Cancelado": 1, "Finalizado": 0, "Titulo": "Dolor de cabeza", "Descripcion": "Me duele la cabeza."}, {"ID": 22, "Clinica_ID": 1, "Profesional_Matricula": 1, "Cod_Paciente": 1, "Practica_ID": 3, "Fecha_Reserva": "2020-12-19 12:27", "Fecha_Turno": "2020-12-22 13:00", "Notificado": 0, "Cancelado": 0, "Finalizado": 1, "Titulo": "2", "Descripcion": ""}, {"ID": 23, "Clinica_ID": 1, "Profesional_Matricula": 1, "Cod_Paciente": 1, "Practica_ID": 3, "Fecha_Reserva": "2020-12-19 12:27", "Fecha_Turno": "2020-12-22 14:00", "Notificado": 0, "Cancelado": 0, "Finalizado": 1, "Titulo": "3", "Descripcion": ""}, {"ID": 24, "Clinica_ID": 1, "Profesional_Matricula": 1, "Cod_Paciente": 1, "Practica_ID": 3, "Fecha_Reserva": "2020-12-19 12:27", "Fecha_Turno": "2020-12-22 15:00", "Notificado": 0, "Cancelado": 0, "Finalizado": 1, "Titulo": "4", "Descripcion": ""}, {"ID": 25, "Clinica_ID": 1, "Profesional_Matricula": 1, "Cod_Paciente": 1, "Practica_ID": 3, "Fecha_Reserva": "2020-12-19 12:27", "Fecha_Turno": "2020-12-22 17:00", "Notificado": 0, "Cancelado": 0, "Finalizado": 1, "Titulo": "45", "Descripcion": ""}, {"ID": 26, "Clinica_ID": 1, "Profesional_Matricula": 1, "Cod_Paciente": 1, "Practica_ID": 3, "Fecha_Reserva": "2020-12-19 12:28", "Fecha_Turno": "2020-12-22 18:00", "Notificado": 0, "Cancelado": 0, "Finalizado": 1, "Titulo": "33", "Descripcion": ""}, {"ID": 27, "Clinica_ID": 1, "Profesional_Matricula": 1, "Cod_Paciente": 1, "Practica_ID": 3, "Fecha_Reserva": "2020-12-19 12:28", "Fecha_Turno": "2020-12-22 19:00", "Notificado": 0, "Cancelado": 0, "Finalizado": 1, "Titulo": "23234234", "Descripcion": "323234"}, {"ID": 28, "Clinica_ID": 1, "Profesional_Matricula": 1, "Cod_Paciente": 1, "Practica_ID": 3, "Fecha_Reserva": "2020-12-19 16:57", "Fecha_Turno": "2020-12-22 15:00", "Notificado": 0, "Cancelado": 0, "Finalizado": 0, "Titulo": "Se siente mal", "Descripcion": "Anda mal."}]}
          #{"clinicID": 1, "professionalID": 2, "codClient": 76, "practiceID": 4, "reservationDate": "25-11-2020 12:00", "appointmentDay": "25-11-2020 12:00", "notified": 0, "cancelled": 0, "finalized": 0, "title": "Dolor de cabeza", "description": "Migraña"}
    """
    clinicID = request.args.get('clinicID')
    professionalID = request.args.get('professionalID')


    # Get items from the helper
    status = helper.get_professional_events_byClinic(clinicID,professionalID)

    # Return 404 if item not found
    if status is None:
        respuesta = {"error":"Professional not found (clinicID = " + str(clinicID) + " professionalID = " + str(professionalID) + ")."}
        response = Response(json.dumps(respuesta), status=404 , mimetype='application/json')
        return response

    # Return status
    """res_data = {
        'status': status
    }"""

    response = Response(json.dumps(status), status=200, mimetype='application/json')
    return response

#Obtiene todos los turnos de un profesional no cancelados ni finalizados. Próximos a la fecha actual.
@app.route('/events/getProfessionalEventsNotCancelled', methods=['GET'])
def get_professional_events_not_cancelled():
    """Gets all the not cancelled events for a specified professional in a specific clinic.
    Gets all the not cancelled events for a specified professional in a specific clinic.
    ---
    tags:
      - events
    parameters:
      - name: professionalID
        in: query
        type: integer
        #enum: ['all', 'rgb', 'cmyk']
        required: true
        #default: 1
        description: Professional's ID.
      - name: clinicID
        in: query
        type: integer
        #enum: ['all', 'rgb', 'cmyk']
        required: true
        #default: 3
        description: Clinic's ID.
    definitions:
      Event:
        type: object
        properties:
          ID:
            type: integer
          Clinica_ID:
            type: integer
          Profesional_Matricula:
            type: integer
          Cod_Paciente:
            type: integer
          Practica_ID:
            type: integer
          Fecha_Reserva:
            type: string
          Fecha_Turno:
            type: string
          Notificado:
            type: integer
          Cancelado:
            type: integer
          Finalizado:
            type: string
          Titulo:
            type: string
          Descripcion:
            type: string
      Events:
        type: object
        properties:
          error:
            type: integer
          status:
            type: array
            items:
              $ref: '#/definitions/Event'
      #Palette:
      #  type: object
      #  properties:
      #    palette_name:
      #      type: array
      #      items:
      #        $ref: '#/definitions/Color'
      #Color:
      #  type: string
    responses:
      200:
        description: The error code and status. An error code of "0" means success.
        schema:
          $ref: '#/definitions/Events'
        examples:
          #{"error": 0, "status": 'Success'}
          {"error": 0, "status": [{"ID": 1, "Clinica_ID": 1, "Profesional_Matricula": 123456, "Cod_Paciente": 1, "Practica_ID": 1, "Fecha_Reserva": "11-11-2020 18:48", "Fecha_Turno": "2020-11-24 12:00", "Notificado": 0, "Cancelado": 1, "Finalizado": 0, "Titulo": "Limprieza para los dientes", "Descripcion": "Estan muy sucios"}, {"ID": 2, "Clinica_ID": 1, "Profesional_Matricula": 1, "Cod_Paciente": 1, "Practica_ID": 3, "Fecha_Reserva": "2020-11-11", "Fecha_Turno": "2020-11-26 20:34", "Notificado": 0, "Cancelado": 0, "Finalizado": 0, "Titulo": "Consulta con Dios", "Descripcion": "Solo Dios sabe"}, {"ID": 3, "Clinica_ID": 1, "Profesional_Matricula": 123456, "Cod_Paciente": 1, "Practica_ID": 1, "Fecha_Reserva": "25-11-2020 12:00", "Fecha_Turno": "2020-11-25 13:00", "Notificado": 0, "Cancelado": 0, "Finalizado": 0, "Titulo": "Esto es una prueba", "Descripcion": "Prueba UPDATE"}, {"ID": 4, "Clinica_ID": 1, "Profesional_Matricula": 123456, "Cod_Paciente": 1, "Practica_ID": 1, "Fecha_Reserva": "25-11-2020 11:00", "Fecha_Turno": "2020-11-25 14:00", "Notificado": 0, "Cancelado": 0, "Finalizado": 0, "Titulo": "Esto es una prueba222", "Descripcion": "Pruebaaaaa"}, {"ID": 5, "Clinica_ID": 1, "Profesional_Matricula": 123456, "Cod_Paciente": 1, "Practica_ID": 1, "Fecha_Reserva": "25-11-2020 12:00", "Fecha_Turno": "2020-11-19 18:00", "Notificado": 0, "Cancelado": 0, "Finalizado": 0, "Titulo": "Esto es una prueba", "Descripcion": "Prueba consulta"}, {"ID": 6, "Clinica_ID": 3, "Profesional_Matricula": 1, "Cod_Paciente": 1, "Practica_ID": 3, "Fecha_Reserva": "2020-11-26 20:00", "Fecha_Turno": "2020-11-27 21:00", "Notificado": 0, "Cancelado": 0, "Finalizado": 0, "Titulo": "Este es el t\u00edtulo.", "Descripcion": "Esta es la descripci\u00f3n."}, {"ID": 7, "Clinica_ID": 1, "Profesional_Matricula": 1, "Cod_Paciente": 1, "Practica_ID": 3, "Fecha_Reserva": "2020-11-27 14:54", "Fecha_Turno": "2020-11-30 12:00", "Notificado": 0, "Cancelado": 1, "Finalizado": 0, "Titulo": "Razon", "Descripcion": "Esta todo mal"}, {"ID": 8, "Clinica_ID": 1, "Profesional_Matricula": 1, "Cod_Paciente": 1, "Practica_ID": 3, "Fecha_Reserva": "2020-11-27 14:59", "Fecha_Turno": "2020-11-30 13:00", "Notificado": 0, "Cancelado": 1, "Finalizado": 0, "Titulo": "mallllll", "Descripcion": "Malisimo"}, {"ID": 9, "Clinica_ID": 1, "Profesional_Matricula": 1, "Cod_Paciente": 1, "Practica_ID": 3, "Fecha_Reserva": "2020-11-27 15:02", "Fecha_Turno": "2020-11-30 17:00", "Notificado": 0, "Cancelado": 1, "Finalizado": 0, "Titulo": "Esta m,al", "Descripcion": "asndasd"}, {"ID": 10, "Clinica_ID": 1, "Profesional_Matricula": 1, "Cod_Paciente": 1, "Practica_ID": 3, "Fecha_Reserva": "2020-11-27 15:06", "Fecha_Turno": "2020-11-30 15:00", "Notificado": 0, "Cancelado": 1, "Finalizado": 0, "Titulo": "asdjkl", "Descripcion": "asjdkl"}, {"ID": 11, "Clinica_ID": 1, "Profesional_Matricula": 1, "Cod_Paciente": 1, "Practica_ID": 3, "Fecha_Reserva": "2020-11-27 15:13", "Fecha_Turno": "2020-11-30 18:00", "Notificado": 0, "Cancelado": 1, "Finalizado": 0, "Titulo": "asddas", "Descripcion": "dddddddddddddddd"}, {"ID": 12, "Clinica_ID": 1, "Profesional_Matricula": 1, "Cod_Paciente": 1, "Practica_ID": 3, "Fecha_Reserva": "2020-11-27 15:28", "Fecha_Turno": "2020-11-30 11:00", "Notificado": 0, "Cancelado": 0, "Finalizado": 0, "Titulo": "Pruebaaaaa", "Descripcion": "234423234234"}, {"ID": 13, "Clinica_ID": 1, "Profesional_Matricula": 1, "Cod_Paciente": 1, "Practica_ID": 3, "Fecha_Reserva": "2020-11-27 15:35", "Fecha_Turno": "2020-12-02 11:00", "Notificado": 0, "Cancelado": 1, "Finalizado": 0, "Titulo": "Dolor de cabeza", "Descripcion": "Me duele la cabeza."}, {"ID": 15, "Clinica_ID": 1, "Profesional_Matricula": 1, "Cod_Paciente": 1, "Practica_ID": 3, "Fecha_Reserva": "2020-11-27 17:36", "Fecha_Turno": "2020-12-04 15:00", "Notificado": 0, "Cancelado": 1, "Finalizado": 0, "Titulo": "Dolor de cabeza", "Descripcion": "Me duele la cabeza."}, {"ID": 22, "Clinica_ID": 1, "Profesional_Matricula": 1, "Cod_Paciente": 1, "Practica_ID": 3, "Fecha_Reserva": "2020-12-19 12:27", "Fecha_Turno": "2020-12-22 13:00", "Notificado": 0, "Cancelado": 0, "Finalizado": 1, "Titulo": "2", "Descripcion": ""}, {"ID": 23, "Clinica_ID": 1, "Profesional_Matricula": 1, "Cod_Paciente": 1, "Practica_ID": 3, "Fecha_Reserva": "2020-12-19 12:27", "Fecha_Turno": "2020-12-22 14:00", "Notificado": 0, "Cancelado": 0, "Finalizado": 1, "Titulo": "3", "Descripcion": ""}, {"ID": 24, "Clinica_ID": 1, "Profesional_Matricula": 1, "Cod_Paciente": 1, "Practica_ID": 3, "Fecha_Reserva": "2020-12-19 12:27", "Fecha_Turno": "2020-12-22 15:00", "Notificado": 0, "Cancelado": 0, "Finalizado": 1, "Titulo": "4", "Descripcion": ""}, {"ID": 25, "Clinica_ID": 1, "Profesional_Matricula": 1, "Cod_Paciente": 1, "Practica_ID": 3, "Fecha_Reserva": "2020-12-19 12:27", "Fecha_Turno": "2020-12-22 17:00", "Notificado": 0, "Cancelado": 0, "Finalizado": 1, "Titulo": "45", "Descripcion": ""}, {"ID": 26, "Clinica_ID": 1, "Profesional_Matricula": 1, "Cod_Paciente": 1, "Practica_ID": 3, "Fecha_Reserva": "2020-12-19 12:28", "Fecha_Turno": "2020-12-22 18:00", "Notificado": 0, "Cancelado": 0, "Finalizado": 1, "Titulo": "33", "Descripcion": ""}, {"ID": 27, "Clinica_ID": 1, "Profesional_Matricula": 1, "Cod_Paciente": 1, "Practica_ID": 3, "Fecha_Reserva": "2020-12-19 12:28", "Fecha_Turno": "2020-12-22 19:00", "Notificado": 0, "Cancelado": 0, "Finalizado": 1, "Titulo": "23234234", "Descripcion": "323234"}, {"ID": 28, "Clinica_ID": 1, "Profesional_Matricula": 1, "Cod_Paciente": 1, "Practica_ID": 3, "Fecha_Reserva": "2020-12-19 16:57", "Fecha_Turno": "2020-12-22 15:00", "Notificado": 0, "Cancelado": 0, "Finalizado": 0, "Titulo": "Se siente mal", "Descripcion": "Anda mal."}]}
          #{"clinicID": 1, "professionalID": 2, "codClient": 76, "practiceID": 4, "reservationDate": "25-11-2020 12:00", "appointmentDay": "25-11-2020 12:00", "notified": 0, "cancelled": 0, "finalized": 0, "title": "Dolor de cabeza", "description": "Migraña"}
    """
    clinicID = request.args.get('clinicID')
    professionalID = request.args.get('professionalID')


    # Get items from the helper
    status = helper.get_professional_events_not_cancelled(clinicID,professionalID)

    # Return 404 if item not found
    if status is None:
        respuesta = {"error":"Professional not found (clinicID = " + str(clinicID) + " professionalID = " + str(professionalID) + ")."}
        response = Response(json.dumps(respuesta), status=404 , mimetype='application/json')
        return response

    response = Response(json.dumps(status), status=200, mimetype='application/json')
    return response



#Obtiene los turnos de un profesional en un dia particular
@app.route('/events/getProfessionalDayEvents', methods=['POST'])
def get_professional_day_events():
    """Gets all the not cancelled events for a specified professional in a specific clinic between two dates.
    Gets all the not cancelled events for a specified professional in a specific clinic between two dates.
    ---
    tags:
      - events
    post:
      summary: JSON object containing clinicID, professionalID, beginDate and finishDate.
      #in: header
      #type: object
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/definitions/professionalDayEventsBody'
        required: true
      #default: { "clinicID": 1, "professionalID": 1, "beginDate": "", "finishDate": "" }
        
    definitions:
      professionalDayEventsBody:
        type: object
        properties:
          clinicID:
            type: integer
          professionalID:
            type: integer
          beginDate:
            string
          finishDate:
            string
      Event:
        type: object
        properties:
          ID:
            type: integer
          Clinica_ID:
            type: integer
          Profesional_Matricula:
            type: integer
          Cod_Paciente:
            type: integer
          Practica_ID:
            type: integer
          Fecha_Reserva:
            type: string
          Fecha_Turno:
            type: string
          Notificado:
            type: integer
          Cancelado:
            type: integer
          Finalizado:
            type: string
          Titulo:
            type: string
          Descripcion:
            type: string
      Events:
        type: object
        properties:
          error:
            type: integer
          status:
            type: array
            items:
              $ref: '#/definitions/Event'
      #Palette:
      #  type: object
      #  properties:
      #    palette_name:
      #      type: array
      #      items:
      #        $ref: '#/definitions/Color'
      #Color:
      #  type: string
    responses:
      200:
        description: The error code and status. An error code of "0" means success.
        schema:
          $ref: '#/definitions/Events'
        examples:
          #{"error": 0, "status": 'Success'}
          {"error": 0, "status": [{"ID": 1, "Clinica_ID": 1, "Profesional_Matricula": 123456, "Cod_Paciente": 1, "Practica_ID": 1, "Fecha_Reserva": "11-11-2020 18:48", "Fecha_Turno": "2020-11-24 12:00", "Notificado": 0, "Cancelado": 1, "Finalizado": 0, "Titulo": "Limprieza para los dientes", "Descripcion": "Estan muy sucios"}, {"ID": 2, "Clinica_ID": 1, "Profesional_Matricula": 1, "Cod_Paciente": 1, "Practica_ID": 3, "Fecha_Reserva": "2020-11-11", "Fecha_Turno": "2020-11-26 20:34", "Notificado": 0, "Cancelado": 0, "Finalizado": 0, "Titulo": "Consulta con Dios", "Descripcion": "Solo Dios sabe"}, {"ID": 3, "Clinica_ID": 1, "Profesional_Matricula": 123456, "Cod_Paciente": 1, "Practica_ID": 1, "Fecha_Reserva": "25-11-2020 12:00", "Fecha_Turno": "2020-11-25 13:00", "Notificado": 0, "Cancelado": 0, "Finalizado": 0, "Titulo": "Esto es una prueba", "Descripcion": "Prueba UPDATE"}, {"ID": 4, "Clinica_ID": 1, "Profesional_Matricula": 123456, "Cod_Paciente": 1, "Practica_ID": 1, "Fecha_Reserva": "25-11-2020 11:00", "Fecha_Turno": "2020-11-25 14:00", "Notificado": 0, "Cancelado": 0, "Finalizado": 0, "Titulo": "Esto es una prueba222", "Descripcion": "Pruebaaaaa"}, {"ID": 5, "Clinica_ID": 1, "Profesional_Matricula": 123456, "Cod_Paciente": 1, "Practica_ID": 1, "Fecha_Reserva": "25-11-2020 12:00", "Fecha_Turno": "2020-11-19 18:00", "Notificado": 0, "Cancelado": 0, "Finalizado": 0, "Titulo": "Esto es una prueba", "Descripcion": "Prueba consulta"}, {"ID": 6, "Clinica_ID": 3, "Profesional_Matricula": 1, "Cod_Paciente": 1, "Practica_ID": 3, "Fecha_Reserva": "2020-11-26 20:00", "Fecha_Turno": "2020-11-27 21:00", "Notificado": 0, "Cancelado": 0, "Finalizado": 0, "Titulo": "Este es el t\u00edtulo.", "Descripcion": "Esta es la descripci\u00f3n."}, {"ID": 7, "Clinica_ID": 1, "Profesional_Matricula": 1, "Cod_Paciente": 1, "Practica_ID": 3, "Fecha_Reserva": "2020-11-27 14:54", "Fecha_Turno": "2020-11-30 12:00", "Notificado": 0, "Cancelado": 1, "Finalizado": 0, "Titulo": "Razon", "Descripcion": "Esta todo mal"}, {"ID": 8, "Clinica_ID": 1, "Profesional_Matricula": 1, "Cod_Paciente": 1, "Practica_ID": 3, "Fecha_Reserva": "2020-11-27 14:59", "Fecha_Turno": "2020-11-30 13:00", "Notificado": 0, "Cancelado": 1, "Finalizado": 0, "Titulo": "mallllll", "Descripcion": "Malisimo"}, {"ID": 9, "Clinica_ID": 1, "Profesional_Matricula": 1, "Cod_Paciente": 1, "Practica_ID": 3, "Fecha_Reserva": "2020-11-27 15:02", "Fecha_Turno": "2020-11-30 17:00", "Notificado": 0, "Cancelado": 1, "Finalizado": 0, "Titulo": "Esta m,al", "Descripcion": "asndasd"}, {"ID": 10, "Clinica_ID": 1, "Profesional_Matricula": 1, "Cod_Paciente": 1, "Practica_ID": 3, "Fecha_Reserva": "2020-11-27 15:06", "Fecha_Turno": "2020-11-30 15:00", "Notificado": 0, "Cancelado": 1, "Finalizado": 0, "Titulo": "asdjkl", "Descripcion": "asjdkl"}, {"ID": 11, "Clinica_ID": 1, "Profesional_Matricula": 1, "Cod_Paciente": 1, "Practica_ID": 3, "Fecha_Reserva": "2020-11-27 15:13", "Fecha_Turno": "2020-11-30 18:00", "Notificado": 0, "Cancelado": 1, "Finalizado": 0, "Titulo": "asddas", "Descripcion": "dddddddddddddddd"}, {"ID": 12, "Clinica_ID": 1, "Profesional_Matricula": 1, "Cod_Paciente": 1, "Practica_ID": 3, "Fecha_Reserva": "2020-11-27 15:28", "Fecha_Turno": "2020-11-30 11:00", "Notificado": 0, "Cancelado": 0, "Finalizado": 0, "Titulo": "Pruebaaaaa", "Descripcion": "234423234234"}, {"ID": 13, "Clinica_ID": 1, "Profesional_Matricula": 1, "Cod_Paciente": 1, "Practica_ID": 3, "Fecha_Reserva": "2020-11-27 15:35", "Fecha_Turno": "2020-12-02 11:00", "Notificado": 0, "Cancelado": 1, "Finalizado": 0, "Titulo": "Dolor de cabeza", "Descripcion": "Me duele la cabeza."}, {"ID": 15, "Clinica_ID": 1, "Profesional_Matricula": 1, "Cod_Paciente": 1, "Practica_ID": 3, "Fecha_Reserva": "2020-11-27 17:36", "Fecha_Turno": "2020-12-04 15:00", "Notificado": 0, "Cancelado": 1, "Finalizado": 0, "Titulo": "Dolor de cabeza", "Descripcion": "Me duele la cabeza."}, {"ID": 22, "Clinica_ID": 1, "Profesional_Matricula": 1, "Cod_Paciente": 1, "Practica_ID": 3, "Fecha_Reserva": "2020-12-19 12:27", "Fecha_Turno": "2020-12-22 13:00", "Notificado": 0, "Cancelado": 0, "Finalizado": 1, "Titulo": "2", "Descripcion": ""}, {"ID": 23, "Clinica_ID": 1, "Profesional_Matricula": 1, "Cod_Paciente": 1, "Practica_ID": 3, "Fecha_Reserva": "2020-12-19 12:27", "Fecha_Turno": "2020-12-22 14:00", "Notificado": 0, "Cancelado": 0, "Finalizado": 1, "Titulo": "3", "Descripcion": ""}, {"ID": 24, "Clinica_ID": 1, "Profesional_Matricula": 1, "Cod_Paciente": 1, "Practica_ID": 3, "Fecha_Reserva": "2020-12-19 12:27", "Fecha_Turno": "2020-12-22 15:00", "Notificado": 0, "Cancelado": 0, "Finalizado": 1, "Titulo": "4", "Descripcion": ""}, {"ID": 25, "Clinica_ID": 1, "Profesional_Matricula": 1, "Cod_Paciente": 1, "Practica_ID": 3, "Fecha_Reserva": "2020-12-19 12:27", "Fecha_Turno": "2020-12-22 17:00", "Notificado": 0, "Cancelado": 0, "Finalizado": 1, "Titulo": "45", "Descripcion": ""}, {"ID": 26, "Clinica_ID": 1, "Profesional_Matricula": 1, "Cod_Paciente": 1, "Practica_ID": 3, "Fecha_Reserva": "2020-12-19 12:28", "Fecha_Turno": "2020-12-22 18:00", "Notificado": 0, "Cancelado": 0, "Finalizado": 1, "Titulo": "33", "Descripcion": ""}, {"ID": 27, "Clinica_ID": 1, "Profesional_Matricula": 1, "Cod_Paciente": 1, "Practica_ID": 3, "Fecha_Reserva": "2020-12-19 12:28", "Fecha_Turno": "2020-12-22 19:00", "Notificado": 0, "Cancelado": 0, "Finalizado": 1, "Titulo": "23234234", "Descripcion": "323234"}, {"ID": 28, "Clinica_ID": 1, "Profesional_Matricula": 1, "Cod_Paciente": 1, "Practica_ID": 3, "Fecha_Reserva": "2020-12-19 16:57", "Fecha_Turno": "2020-12-22 15:00", "Notificado": 0, "Cancelado": 0, "Finalizado": 0, "Titulo": "Se siente mal", "Descripcion": "Anda mal."}]}
          #{"clinicID": 1, "professionalID": 2, "codClient": 76, "practiceID": 4, "reservationDate": "25-11-2020 12:00", "appointmentDay": "25-11-2020 12:00", "notified": 0, "cancelled": 0, "finalized": 0, "title": "Dolor de cabeza", "description": "Migraña"}
    """
    req_data = request.get_json()
    clinicID = req_data['clinicID']
    professionalID = req_data['professionalID']
    beginDate = req_data['beginDate']
    finishDate = req_data['finishDate']
    data = [clinicID,professionalID,beginDate,finishDate]
    

    # Get items from the helper
    status = helper.get_professional_day_events(data)

    # Return 404 if item not found
    if status is None:
        respuesta = {"error":"Schedule not found (clinicID = " + str(clinicID) + " professionalID = " + str(professionalID) + ")."}
        response = Response(json.dumps(respuesta), status=404 , mimetype='application/json')
        return response

    # Return status
    """res_data = {
        'status': status
    }"""

    response = Response(json.dumps(status), status=200, mimetype='application/json')
    return response






#Obtiene los el horario de un profesional todos los dias
@app.route('/events/getProfessionalSchedule', methods=['GET'])
def get_professional_schedule():
    """Gets the schedule for a specified professional in a specific clinic.
    Gets the schedule for a specified professional in a specific clinic.
    ---
    tags:
      - professionals
    parameters:
      - name: professionalID
        in: query
        type: integer
        #enum: ['all', 'rgb', 'cmyk']
        required: true
        #default: 1
        description: Professional's ID.
      - name: clinicID
        in: query
        type: integer
        #enum: ['all', 'rgb', 'cmyk']
        required: true
        #default: 3
        description: Clinic's ID.
    definitions:
      WorkingHours:
        type: object
        properties:
          Dia:
            type: integer
          Horario_Inicio:
            type: string
          Horario_Fin:
            type: string
      Schedule:
        type: object
        properties:
          error:
            type: integer
          status:
            type: array
            items:
              $ref: '#/definitions/WorkingHours'
    responses:
      200:
        description: The error code and status. An error code of "0" means success.
        schema:
          $ref: '#/definitions/Schedule'
        examples:
          #{"error": 0, "status": 'Success'}
          #{"clinicID": 1, "professionalID": 2, "codClient": 76, "practiceID": 4, "reservationDate": "25-11-2020 12:00", "appointmentDay": "25-11-2020 12:00", "notified": 0, "cancelled": 0, "finalized": 0, "title": "Dolor de cabeza", "description": "Migraña"}
    """
    clinicID = request.args.get('clinicID')
    professionalID = request.args.get('professionalID')


    # Get items from the helper
    status = helper.get_professional_schedule(clinicID,professionalID)

    # Return 404 if item not found
    if status is None:
        respuesta = {"error":"Schedule not found (clinicID = " + str(clinicID) + " professionalID = " + str(professionalID) + ")."}
        response = Response(json.dumps(respuesta), status=404 , mimetype='application/json')
        return response

    # Return status
    """res_data = {
        'status': status
    }"""

    response = Response(json.dumps(status), status=200, mimetype='application/json')
    return response






#Obtiene los el horario de un profesional en un dia particular
@app.route('/events/getProfessionalDaySchedule', methods=['POST'])
def get_professional_day_schedule():
    """Gets the working hours for a specified professional in a specific clinic on a specific date.
    Gets the working hours for a specified professional in a specific clinic on a specific date.
    ---
    tags:
      - professionals
    post:
      summary: JSON object containing clinicID, professionalID, and date.
      #in: header
      #type: object
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties:
                clinicID:
                  type: integer
                professionalID:
                  type: integer
                date:
                  type: string
              example:
                clinicID: 1
                professionalID: 1
                date: 25-12-2020
        required: true
      #default: { "clinicID": 1, "professionalID": 1, "date": "" }
    definitions:
      professionalDayScheduleBody:
        type: object
        properties:
          clinicID:
            type: integer
          professionalID:
            type: integer
          date:
            type: string
      WorkingHoursResponse:
        type: object
        properties:
          error:
            type: integer
          status:
            type: object
            properties:
              Dia:
                type: integer
              Horario_Inicio:
                type: string
              Horario_Fin:
                type: string
            
    responses:
      200:
        description: The error code and status. An error code of "0" means success.
        schema:
          $ref: '#/definitions/WorkingHoursResponse'
        examples:
          error: 0
          status: { "Dia": 0, "Horario_Inicio": "10:00", "Horario_Fin": "20:00" }
          #{"error": 0, "status": 'Success'}
          #{"clinicID": 1, "professionalID": 2, "codClient": 76, "practiceID": 4, "reservationDate": "25-11-2020 12:00", "appointmentDay": "25-11-2020 12:00", "notified": 0, "cancelled": 0, "finalized": 0, "title": "Dolor de cabeza", "description": "Migraña"}
    """
    req_data = request.get_json()
    clinicID = req_data['clinicID']
    professionalID = req_data['professionalID']
    date = req_data['date']
    data = [clinicID,professionalID,date]
    

    # Get items from the helper
    status = helper.get_professional_day_schedule(data)

    # Return 404 if item not found
    if status is None:
        respuesta = {"error":"Schedule not found (clinicID = " + str(clinicID) + " professionalID = " + str(professionalID) + ")."}
        response = Response(json.dumps(respuesta), status=404 , mimetype='application/json')
        return response

    # Return status
    """res_data = {
        'status': status
    }"""

    response = Response(json.dumps(status), status=200, mimetype='application/json')
    return response



#Obtiene todos los turnos pendientes de un cliente
@app.route('/events/getClientPendingEvents', methods=['GET'])
def get_client_pending_events():
    """Gets the pending events for a specified client.
    Gets the pending events for a specified client.
    ---
    tags:
      - events
    parameters:
      - name: clientID
        in: query
        type: integer
        required: true
        #default: 1
        description: Client's ID.
    definitions:
      clientPendingEvent:
        type: object
        properties:
          ID:
            type: integer
          Clinica_ID:
            type: integer
          Profesional_Matricula:
            type: integer
          Cod_Paciente:
            type: integer
          Practica_ID:
            type: integer
          Fecha_Reserva:
            type: string
          Fecha_Turno:
            type: string
          Notificado:
            type: integer
          Cancelado:
            type: integer
          Finalizado:
            type: integer
          Titulo:
            type: string
          Descripcion:
            type: string
          Profesional:
            type: string
          Clinica:
            type: string
      clientPendingEvents:
        type: object
        properties:
          error:
            type: integer
          status:
            type: array
            items:
              #ref: '#/definitions/clientPendingEvent'
    responses:
      200:
        description: The error code and status. An error code of "0" means success.
        schema:
          $ref: '#/definitions/Events'
        examples:
          error: 0
          status: [{"ID": 28, "Clinica_ID": 1, "Profesional_Matricula": 1, "Cod_Paciente": 1, "Practica_ID": 3, "Fecha_Reserva": "2020-12-19 16:57", "Fecha_Turno": "2020-12-22 15:00", "Notificado": 0, "Cancelado": 0, "Finalizado": 0, "Titulo": "Se siente mal", "Descripcion": "Anda mal.", "Profesional": "Gregory House", "Clinica": "Princeton Plainsboro" }]
          #{"error": 0, "status": 'Success'}
          #{"clinicID": 1, "professionalID": 2, "codClient": 76, "practiceID": 4, "reservationDate": "25-11-2020 12:00", "appointmentDay": "25-11-2020 12:00", "notified": 0, "cancelled": 0, "finalized": 0, "title": "Dolor de cabeza", "description": "Migraña"}
    """
    clientID = request.args.get('clientID')

    # Get items from the helper
    status = helper.get_client_pending_events(clientID)

    # Return 404 if item not found
    if status is None:
        respuesta = {"error":"Client not found (clientID=" + str(clientID) + ")."}
        response = Response(json.dumps(respuesta), status=404 , mimetype='application/json')
        return response

    # Return status
    """res_data = {
        'status': status
    }"""

    response = Response(json.dumps(status), status=200, mimetype='application/json')
    return response

#Obtiene todas las especialidades
@app.route('/events/getSpecialities', methods=['GET'])
def get_specialities():
    """Gets all the specialities.
    Gets all the specialities.
    ---
    tags:
      - specialities
    definitions:
      Speciality:
        type: object
        properties:
          ID:
            type: integer
          Nombre:
            type: string
      Specialities:
        type: object
        properties:
          error:
            type: integer
          status:
            type: array
            items:
              $ref: '#/definitions/Speciality'
    responses:
      200:
        description: The error code and status. An error code of "0" means success.
        schema:
          $ref: '#/definitions/Specialities'
        examples:
          error: 0
          status: [ {"ID": 0, "Nombre": "Especialidad1"} ]
    """

    # Get items from the helper
    status = helper.get_specialities()

    # Return 404 if item not found
    if status is None:
        respuesta = {"error":"Hubo un error."}
        response = Response(json.dumps(respuesta), status=404 , mimetype='application/json')
        return response

    # Return status
    """res_data = {
        'status': status
    }"""

    response = Response(json.dumps(status), status=200, mimetype='application/json')
    return response

#Obtiene todas las prácticas
@app.route('/events/getPractices', methods=['GET'])
def get_practices():
    """Gets all the practices.
    Gets all the practices.
    ---
    tags:
      - practices
    definitions:
      Practice:
        type: object
        properties:
          ID:
            type: integer
          Nombre:
            type: string
          Duracion_Turno:
            type: integer
          Especialidad_ID:
            type: integer
      Practices:
        type: object
        properties:
          error:
            type: integer
          status:
            type: array
            items:
              $ref: '#/definitions/Practice'
    responses:
      200:
        description: The error code and status. An error code of "0" means success.
        schema:
          $ref: '#/definitions/Practices'
        examples:
          #error: 0
          #status: [ {"ID": 0, "Nombre": "Especialidad1"} ]
    """

    # Get items from the helper
    status = helper.get_practices()

    # Return 404 if item not found
    if status is None:
        respuesta = {"error":"Hubo un error."}
        response = Response(json.dumps(respuesta), status=404 , mimetype='application/json')
        return response

    # Return status
    """res_data = {
        'status': status
    }"""

    response = Response(json.dumps(status), status=200, mimetype='application/json')
    return response

#Obtiene todas las prácticas según especialidades
@app.route('/events/getPracticesBySpecialities', methods=['GET'])
def get_practices_by_specialities():
    """Gets practices by specialityID.
    Gets practices by specialityID.
    ---
    tags:
      - practices
    parameters:
      - name: specialityID
        in: query
        type: integer
        required: true
        #default: 1
        description: The ID of a speciality.
    responses:
      200:
        description: The error code and status. An error code of "0" means success.
        schema:
          $ref: '#/definitions/Practices'
        examples:
          ejemplo:
            summary: Un ejemplo.
            value:
              error: 0
              status: [{"ID": 28, "Clinica_ID": 1, "Profesional_Matricula": 1, "Cod_Paciente": 1, "Practica_ID": 3, "Fecha_Reserva": "2020-12-19 16:57", "Fecha_Turno": "2020-12-22 15:00", "Notificado": 0, "Cancelado": 0, "Finalizado": 0, "Titulo": "Se siente mal", "Descripcion": "Anda mal.", "Profesional": "Gregory House", "Clinica": "Princeton Plainsboro" }]
          #{"error": 0, "status": 'Success'}
          #{"clinicID": 1, "professionalID": 2, "codClient": 76, "practiceID": 4, "reservationDate": "25-11-2020 12:00", "appointmentDay": "25-11-2020 12:00", "notified": 0, "cancelled": 0, "finalized": 0, "title": "Dolor de cabeza", "description": "Migraña"}
    """
    specialityID = request.args.get('specialityID')

    # Get items from the helper
    status = helper.get_practices_by_specialities(specialityID)

    # Return 404 if item not found
    if status is None:
        respuesta = {"error":"Hubo un error."}
        response = Response(json.dumps(respuesta), status=404 , mimetype='application/json')
        return response

    # Return status
    """res_data = {
        'status': status
    }"""

    response = Response(json.dumps(status), status=200, mimetype='application/json')
    return response

#Obtiene todos los profesionales
@app.route('/events/getProfessionals', methods=['GET'])
def get_professionals():
    """Gets all the professionals.
    Gets all the professionals.
    ---
    tags:
      - professionals
    #parameters:
    #  - name: specialityID
    #    in: query
    #    type: integer
    #    required: true
    #    #default: 1
    #    description: The ID of a speciality.
    definitions:
      Professional:
        type: object
        properties:
          Matricula:
            type: integer
          Especialidad_ID:
            type: integer
          Activo:
            type: integer
          Nombre:
            type: string
          DNI:
            type: integer
          Telefono:
            type: integer
          Email:
            type: string
      Professionals:
        type: object
        properties:
          error:
            type: integer
          status:
            type: array
            items:
              $ref: '#/definitions/Professional'
    responses:
      200:
        description: The error code and status. An error code of "0" means success.
        schema:
          $ref: '#/definitions/Professionals'
        examples:
          #error: 0
          #status: [{"ID": 28, "Clinica_ID": 1, "Profesional_Matricula": 1, "Cod_Paciente": 1, "Practica_ID": 3, "Fecha_Reserva": "2020-12-19 16:57", "Fecha_Turno": "2020-12-22 15:00", "Notificado": 0, "Cancelado": 0, "Finalizado": 0, "Titulo": "Se siente mal", "Descripcion": "Anda mal.", "Profesional": "Gregory House", "Clinica": "Princeton Plainsboro" }]
          #{"error": 0, "status": 'Success'}
          #{"clinicID": 1, "professionalID": 2, "codClient": 76, "practiceID": 4, "reservationDate": "25-11-2020 12:00", "appointmentDay": "25-11-2020 12:00", "notified": 0, "cancelled": 0, "finalized": 0, "title": "Dolor de cabeza", "description": "Migraña"}
    """

    # Get items from the helper
    status = helper.get_professionals()

    # Return 404 if item not found
    if status is None:
        respuesta = {"error":"Hubo un error."}
        response = Response(json.dumps(respuesta), status=404 , mimetype='application/json')
        return response

    # Return status
    """res_data = {
        'status': status
    }"""

    response = Response(json.dumps(status), status=200, mimetype='application/json')
    return response





    #Obtiene todos los pacintes
@app.route('/events/getClients', methods=['GET'])
def get_clients():
    """Gets all the clients.
    Gets all the clients.
    ---
    tags:
      - clients
    #parameters:
    #  - name: specialityID
    #    in: query
    #    type: integer
    #    required: true
    #    #default: 1
    #    description: The ID of a speciality.
    definitions:
      Client:
        type: object
        properties:
          Cod_Paciente:
            type: integer
          Usuario_ID:
            type: integer
          Nombre:
            type: string
          DNI:
            type: integer
          Telefono:
            type: integer
          Email:
            type: string
      Clients:
        type: object
        properties:
          error:
            type: integer
          status:
            type: array
            items:
              $ref: '#/definitions/Client'
    responses:
      200:
        description: The error code and status. An error code of "0" means success.
        schema:
          $ref: '#/definitions/Clients'
        examples:
          #error: 0
          #status: [{"ID": 28, "Clinica_ID": 1, "Profesional_Matricula": 1, "Cod_Paciente": 1, "Practica_ID": 3, "Fecha_Reserva": "2020-12-19 16:57", "Fecha_Turno": "2020-12-22 15:00", "Notificado": 0, "Cancelado": 0, "Finalizado": 0, "Titulo": "Se siente mal", "Descripcion": "Anda mal.", "Profesional": "Gregory House", "Clinica": "Princeton Plainsboro" }]
          #{"error": 0, "status": 'Success'}
          #{"clinicID": 1, "professionalID": 2, "codClient": 76, "practiceID": 4, "reservationDate": "25-11-2020 12:00", "appointmentDay": "25-11-2020 12:00", "notified": 0, "cancelled": 0, "finalized": 0, "title": "Dolor de cabeza", "description": "Migraña"}
    """

    # Get items from the helper
    status = helper.get_clients()

    # Return 404 if item not found
    if status is None:
        respuesta = {"error":"Hubo un error."}
        response = Response(json.dumps(respuesta), status=404 , mimetype='application/json')
        return response

    # Return status
    """res_data = {
        'status': status
    }"""

    response = Response(json.dumps(status), status=200, mimetype='application/json')
    return response





#Obtiene todos los profesionales por especialidad
@app.route('/events/getProfessionalsBySpecialities', methods=['GET'])
def get_professionals_by_specialities():
    """Gets all the professionals by speciality.
    Gets all the professionals by speciality.
    ---
    tags:
      - professionals
    parameters:
      - name: specialityID
        in: query
        type: integer
        required: true
        #default: 1
        description: The ID of a speciality.
    responses:
      200:
        description: The error code and status. An error code of "0" means success.
        schema:
          $ref: '#/definitions/Professionals'
        examples:
          #error: 0
          #status: [{"ID": 28, "Clinica_ID": 1, "Profesional_Matricula": 1, "Cod_Paciente": 1, "Practica_ID": 3, "Fecha_Reserva": "2020-12-19 16:57", "Fecha_Turno": "2020-12-22 15:00", "Notificado": 0, "Cancelado": 0, "Finalizado": 0, "Titulo": "Se siente mal", "Descripcion": "Anda mal.", "Profesional": "Gregory House", "Clinica": "Princeton Plainsboro" }]
          #{"error": 0, "status": 'Success'}
          #{"clinicID": 1, "professionalID": 2, "codClient": 76, "practiceID": 4, "reservationDate": "25-11-2020 12:00", "appointmentDay": "25-11-2020 12:00", "notified": 0, "cancelled": 0, "finalized": 0, "title": "Dolor de cabeza", "description": "Migraña"}
    """

    specialityID = request.args.get('specialityID')

    # Get items from the helper
    status = helper.get_professionals_by_specialities(specialityID)

    # Return 404 if item not found
    if status is None:
        respuesta = {"error":"Hubo un error."}
        response = Response(json.dumps(respuesta), status=404 , mimetype='application/json')
        return response

    # Return status
    """res_data = {
        'status': status
    }"""

    response = Response(json.dumps(status), status=200, mimetype='application/json')
    return response





#Obtiene todas las clínicas
@app.route('/events/getClinics', methods=['GET'])
def get_clinics():
    """Gets all the clinics.
    Gets all the clinics.
    ---
    tags:
      - clinics
    definitions:
      Clinic:
        type: object
        properties:
          ID:
            type: integer
          Nombre:
            type: string
          Direccion:
            type: string
          Telefono:
            type: integer
      Clinics:
        type: object
        properties:
          error:
            type: integer
          status:
            type: array
            items:
              $ref: '#/definitions/Clinic'
    responses:
      200:
        description: The error code and status. An error code of "0" means success.
        schema:
          $ref: '#/definitions/Clinics'
        examples:
          #error: 0
          #status: [{"ID": 28, "Clinica_ID": 1, "Profesional_Matricula": 1, "Cod_Paciente": 1, "Practica_ID": 3, "Fecha_Reserva": "2020-12-19 16:57", "Fecha_Turno": "2020-12-22 15:00", "Notificado": 0, "Cancelado": 0, "Finalizado": 0, "Titulo": "Se siente mal", "Descripcion": "Anda mal.", "Profesional": "Gregory House", "Clinica": "Princeton Plainsboro" }]
          #{"error": 0, "status": 'Success'}
          #{"clinicID": 1, "professionalID": 2, "codClient": 76, "practiceID": 4, "reservationDate": "25-11-2020 12:00", "appointmentDay": "25-11-2020 12:00", "notified": 0, "cancelled": 0, "finalized": 0, "title": "Dolor de cabeza", "description": "Migraña"}
    """

    print('Hola')

    # Get items from the helper
    status = helper.get_clinics()

    # Return 404 if item not found
    if status is None:
        respuesta = {"error":"Hubo un error."}
        response = Response(json.dumps(respuesta), status=404 , mimetype='application/json')
        return response

    # Return status
    """res_data = {
        'status': status
    }"""

    response = Response(json.dumps(status), status=200, mimetype='application/json')
    return response

#Obtiene todas las clínicas en las que trabaja cierto profesional
@app.route('/events/getProfessionalsClinics', methods=['GET'])
def get_professionals_clinics():
    """Gets all the clinics where a specific professional works.
    Gets all the clinics where a specific professional works.
    ---
    tags:
      - clinics
    parameters:
      - name: professionalID
        in: query
        type: integer
        required: true
        #default: 1
        description: The ID of a professional.
    responses:
      200:
        description: The error code and status. An error code of "0" means success.
        schema:
          $ref: '#/definitions/Clinics'
        examples:
          #error: 0
          #status: [{"ID": 28, "Clinica_ID": 1, "Profesional_Matricula": 1, "Cod_Paciente": 1, "Practica_ID": 3, "Fecha_Reserva": "2020-12-19 16:57", "Fecha_Turno": "2020-12-22 15:00", "Notificado": 0, "Cancelado": 0, "Finalizado": 0, "Titulo": "Se siente mal", "Descripcion": "Anda mal.", "Profesional": "Gregory House", "Clinica": "Princeton Plainsboro" }]
          #{"error": 0, "status": 'Success'}
          #{"clinicID": 1, "professionalID": 2, "codClient": 76, "practiceID": 4, "reservationDate": "25-11-2020 12:00", "appointmentDay": "25-11-2020 12:00", "notified": 0, "cancelled": 0, "finalized": 0, "title": "Dolor de cabeza", "description": "Migraña"}
    """

    professionalID = request.args.get('professionalID')

    # Get items from the helper
    status = helper.get_professionals_clinics(professionalID)

    # Return 404 if item not found
    if status is None:
        respuesta = {"error":"Hubo un error."}
        response = Response(json.dumps(respuesta), status=404 , mimetype='application/json')
        return response

    # Return status
    """res_data = {
        'status': status
    }"""

    response = Response(json.dumps(status), status=200, mimetype='application/json')
    return response

#Comprueba email y contraseña y devuelve el ID del usuario.
@app.route('/events/login', methods=['GET'])
def login():
    """Checks email and password and returns the user ID.
    Checks email and password and returns the user ID.
    ---
    tags:
      - login
    parameters:
      - name: email
        in: query
        type: string
        required: true
        #default: 1
        description: A user's email.
      - name: password
        in: query
        type: string
        required: true
        #default: 1
        description: The user's password.
    definitions:
      UserID:
        type: object
        properties:
          ID:
            type: integer
      UserIDs:
        type: object
        properties:
          error:
            type: integer
          status:
            type: array
            items:
              $ref: '#/definitions/UserID'
          
    responses:
      200:
        description: The error code and status. An error code of "0" means success.
        schema:
          $ref: '#/definitions/UserIDs'
        examples:
          #error: 0
          #status: [{"ID": 28, "Clinica_ID": 1, "Profesional_Matricula": 1, "Cod_Paciente": 1, "Practica_ID": 3, "Fecha_Reserva": "2020-12-19 16:57", "Fecha_Turno": "2020-12-22 15:00", "Notificado": 0, "Cancelado": 0, "Finalizado": 0, "Titulo": "Se siente mal", "Descripcion": "Anda mal.", "Profesional": "Gregory House", "Clinica": "Princeton Plainsboro" }]
          #{"error": 0, "status": 'Success'}
          #{"clinicID": 1, "professionalID": 2, "codClient": 76, "practiceID": 4, "reservationDate": "25-11-2020 12:00", "appointmentDay": "25-11-2020 12:00", "notified": 0, "cancelled": 0, "finalized": 0, "title": "Dolor de cabeza", "description": "Migraña"}
    """

    email = request.args.get('email')
    password = request.args.get('password')

    # Get items from the helper
    status = helper.login(email, password)

    # Return 404 if item not found
    if status is None:
        respuesta = {"error":"Hubo un error."}
        response = Response(json.dumps(respuesta), status=404 , mimetype='application/json')
        return response

    response = Response(json.dumps(status), status=200, mimetype='application/json')
    return response

#Comprueba si un usuario es médico o no. Si es, devuelve su ID.
#Error = 1 si no es médico.
@app.route('/events/isProfessional', methods=['GET'])
def isProfessional():
    """Checks if a user is a professional by the user ID.
    Checks if a user is a professional by the user ID.
    ---
    tags:
      - users
    parameters:
      - name: userID
        in: query
        type: integer
        required: true
        #default: 1
        description: A user's ID.
    definitions:
      isProfessional:
        type: object
        properties:
          isProfessional:
            type: boolean
          matricula:
            type: integer
          especialidadID:
            type: integer    
    responses:
      200:
        description: The error code and status. An error code of "0" means success.
        schema:
          $ref: '#/definitions/isProfessional'
        examples:
          #error: 0
          #status: [{"ID": 28, "Clinica_ID": 1, "Profesional_Matricula": 1, "Cod_Paciente": 1, "Practica_ID": 3, "Fecha_Reserva": "2020-12-19 16:57", "Fecha_Turno": "2020-12-22 15:00", "Notificado": 0, "Cancelado": 0, "Finalizado": 0, "Titulo": "Se siente mal", "Descripcion": "Anda mal.", "Profesional": "Gregory House", "Clinica": "Princeton Plainsboro" }]
          #{"error": 0, "status": 'Success'}
          #{"clinicID": 1, "professionalID": 2, "codClient": 76, "practiceID": 4, "reservationDate": "25-11-2020 12:00", "appointmentDay": "25-11-2020 12:00", "notified": 0, "cancelled": 0, "finalized": 0, "title": "Dolor de cabeza", "description": "Migraña"}
    """

    userID = request.args.get('userID')

    # Get items from the helper
    status = helper.isProfessional(userID)

    # Return 404 if item not found
    if status is None:
        respuesta = {"error":"Hubo un error."}
        response = Response(json.dumps(respuesta), status=404 , mimetype='application/json')
        return response

    response = Response(json.dumps(status), status=200, mimetype='application/json')
    return response

#si arriba false, consultar acá el Cod_Paciente del cliente
#isPaciente
@app.route('/events/isClient', methods=['GET'])
def isClient():
    """Checks if a user is a client by the user ID.
    Checks if a user is a client by the user ID. Returns "true" if it is, with the codPaciente also.
    ---
    tags:
      - users
    parameters:
      - name: userID
        in: query
        type: integer
        required: true
        #default: 1
        description: A user's ID.
    definitions:
      isClient:
        type: object
        properties:
          isClient:
            type: boolean
          codPaciente:
            type: integer
    responses:
      200:
        description: The error code and status. An error code of "0" means success.
        schema:
          $ref: '#/definitions/isClient'
        examples:
          #error: 0
          #status: [{"ID": 28, "Clinica_ID": 1, "Profesional_Matricula": 1, "Cod_Paciente": 1, "Practica_ID": 3, "Fecha_Reserva": "2020-12-19 16:57", "Fecha_Turno": "2020-12-22 15:00", "Notificado": 0, "Cancelado": 0, "Finalizado": 0, "Titulo": "Se siente mal", "Descripcion": "Anda mal.", "Profesional": "Gregory House", "Clinica": "Princeton Plainsboro" }]
          #{"error": 0, "status": 'Success'}
          #{"clinicID": 1, "professionalID": 2, "codClient": 76, "practiceID": 4, "reservationDate": "25-11-2020 12:00", "appointmentDay": "25-11-2020 12:00", "notified": 0, "cancelled": 0, "finalized": 0, "title": "Dolor de cabeza", "description": "Migraña"}
    """

    userID = request.args.get('userID')

    # Get items from the helper
    status = helper.isClient(userID)

    # Return 404 if item not found
    if status is None:
        respuesta = {"error":"Hubo un error."}
        response = Response(json.dumps(respuesta), status=404 , mimetype='application/json')
        return response

    response = Response(json.dumps(status), status=200, mimetype='application/json')
    return response

#Trae los datos de un usuario
@app.route('/events/getUserData', methods=['GET'])
def get_user_data():
    """Gets all the information of a specific user by userID.
    Returns all the information of a specific user by userID.
    ---
    tags:
      - users
    parameters:
      - name: userID
        in: query
        type: integer
        required: true
        #default: 1
        description: A user's ID.
    definitions:
      User:
        type: object
        properties:
          email:
            type: string
          nombre:
            type: string
          dni:
            type: integer
          telefono:
            type: integer
    responses:
      200:
        description: The error code and status. An error code of "0" means success.
        schema:
          $ref: '#/definitions/User'
        examples:
          #error: 0
          #status: [{"ID": 28, "Clinica_ID": 1, "Profesional_Matricula": 1, "Cod_Paciente": 1, "Practica_ID": 3, "Fecha_Reserva": "2020-12-19 16:57", "Fecha_Turno": "2020-12-22 15:00", "Notificado": 0, "Cancelado": 0, "Finalizado": 0, "Titulo": "Se siente mal", "Descripcion": "Anda mal.", "Profesional": "Gregory House", "Clinica": "Princeton Plainsboro" }]
          #{"error": 0, "status": 'Success'}
          #{"clinicID": 1, "professionalID": 2, "codClient": 76, "practiceID": 4, "reservationDate": "25-11-2020 12:00", "appointmentDay": "25-11-2020 12:00", "notified": 0, "cancelled": 0, "finalized": 0, "title": "Dolor de cabeza", "description": "Migraña"}
    """

    userID = request.args.get('userID')

    # Get items from the helper
    status = helper.get_user_data(userID)

    # Return 404 if item not found
    if status is None:
        respuesta = {"error":"Hubo un error."}
        response = Response(json.dumps(respuesta), status=404 , mimetype='application/json')
        return response

    response = Response(json.dumps(status), status=200, mimetype='application/json')
    return response

#Modifica un usuario
@app.route('/events/editUser', methods=['PUT'])
def editUser():
    """Edits a user information.
    Edits a user information.
    ---
    tags:
      - users
    put:
      summary: Edits a user.
      requestBody:
        $ref: '#/definitions/UserBody'
    definitions:
      UserBody:
        type: object
        properties:
          userID:
            type: integer
          nombre:
            type: string
          dni:
            type: integer
          email:
            type: string
          telefono:
            type: integer
    responses:
      200:
        description: The error code and status. An error code of "0" means success.
        schema:
          $ref: '#/definitions/Response'
        examples:
          #error: 0
          #status: [{"ID": 28, "Clinica_ID": 1, "Profesional_Matricula": 1, "Cod_Paciente": 1, "Practica_ID": 3, "Fecha_Reserva": "2020-12-19 16:57", "Fecha_Turno": "2020-12-22 15:00", "Notificado": 0, "Cancelado": 0, "Finalizado": 0, "Titulo": "Se siente mal", "Descripcion": "Anda mal.", "Profesional": "Gregory House", "Clinica": "Princeton Plainsboro" }]
          #{"error": 0, "status": 'Success'}
          #{"clinicID": 1, "professionalID": 2, "codClient": 76, "practiceID": 4, "reservationDate": "25-11-2020 12:00", "appointmentDay": "25-11-2020 12:00", "notified": 0, "cancelled": 0, "finalized": 0, "title": "Dolor de cabeza", "description": "Migraña"}
    """

    req_data = request.get_json()
    userID = req_data['userID']
    nombre = req_data['nombre']
    dni = req_data['dni']
    email = req_data['email']
    telefono = req_data['telefono']

    data = [userID, nombre, dni, email, telefono]

    

    # Add item to the list
    res_data = helper.edit_user(data)

    # Return error if item not added
    if res_data is None:
        response = Response("{'error': 'User not modified - ID: " + userID + "'}", status=500 , mimetype='application/json')
        return response

    # Return response
    response = Response(json.dumps(res_data), mimetype='application/json')

    return response
    

if __name__ == '__main__':    
    app.run(debug=True, use_reloader=True)