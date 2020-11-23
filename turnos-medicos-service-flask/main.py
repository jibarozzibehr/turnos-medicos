import helper
from flask import Flask, request, Response, json, render_template
from flask_cors import CORS
import json

app = Flask(__name__)
cors = CORS(app, resources={r"*": {"origins": "*"}})


#Agrega un nuevo turno a la db
@app.route('/events/new', methods=['POST'])
def add_event():
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



#Obtiene todos los turnos de un profesional
@app.route('/events/getProfessionalEvents', methods=['GET'])
def get_professional_events():
    clinicID = request.args.get('clinicID')
    professionalID = request.args.get('professionalID')


    # Get items from the helper
    status = helper.get_professional_events(clinicID,professionalID)

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



#Obtiene los turnos de un profesional en un dia particular
@app.route('/events/getProfessionalDayEvents', methods=['POST'])
def get_professional_day_events():
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

#Obtiene todos los profesionales por especialidad
@app.route('/events/getProfessionalsBySpecialities', methods=['GET'])
def get_professionals_by_specialities():
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





    #Obtiene todas las clinicas
@app.route('/events/getClinics', methods=['GET'])
def get_clinics():
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

    

if __name__ == '__main__':    
    app.run(debug=True, use_reloader=True)



