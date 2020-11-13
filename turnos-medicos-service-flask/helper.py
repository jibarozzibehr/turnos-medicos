import sqlite3

DB_PATH = './db.db'
NOTSTARTED = 'Not Started'
INPROGRESS = 'In Progress'
COMPLETED = 'Completed'

import json
import collections

def get_client_events(clientID):
    try:
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute("select * from Turnos where Cod_Paciente=%s" % clientID)
        rows = c.fetchall()
        rowCount = len(rows)
        conn.commit()

        if rowCount == 0:
            return None
            
        objects_list = []
        for row in rows:
            d = collections.OrderedDict()
            d['ID'] = row[0]
            d['Clinica_ID'] = row[1]
            d['Profesional_Matricula'] = row[2]
            d['Cod_Paciente'] = row[3]
            d['Practica_ID'] = row[4]
            d['Fecha_Reserva'] = row[5]
            d['Fecha_Turno'] = row[6]
            d['Notificado'] = row[7]
            d['Cancelado'] = row[8]
            d['Finalizado'] = row[9]
            d['Titulo'] = row[10]
            d['Descripcion'] = row[11]
            objects_list.append(d)
        return objects_list
    except Exception as e:
        print('Error: ', e)
        return None

def add_event(data):
    try:
        clinicID = data[0]
        professionalID = data[1]
        codClient = data[2]
        practiceID = data[3]
        reservationDate = data[4]
        appointmentDay = data[5]
        notified = data[6]
        cancelled = data[7]
        finalized = data[8]
        title = data[9]
        description = data[10]

        conn = sqlite3.connect(DB_PATH)

        # Once a connection has been established, we use the cursor
        # object to execute queries
        c = conn.cursor()

        # Keep the initial status as Not Started
        # c.execute('insert into items(item, status) values(?,?)', (item, NOTSTARTED))

        c.execute('insert into Turnos (Clinica_ID, Profesional_Matricula, Cod_Paciente, Practica_ID, Fecha_Reserva, Fecha_Turno, Notificado, Cancelado, Finalizado, Titulo, Descripcion) values(?,?,?,?,?,?,?,?,?,?,?)', (clinicID, professionalID, codClient, practiceID, reservationDate, appointmentDay, notified, cancelled, finalized, title, description))


        # We commit to save the change
        conn.commit()
        return {"error": 0, "status": 'Success'}
    except Exception as e:
        print('Error: ', e)
        return {"error": 1, "status": e}

def update_event(data):
    try:
        appointmentID = data[0]
        clinicID = data[1]
        professionalID = data[2]
        codClient = data[3]
        practiceID = data[4]
        reservationDate = data[5]
        appointmentDay = data[6]
        notified = data[7]
        cancelled = data[8]
        finalized = data[9]
        title = data[10]
        description = data[11]

        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        
        c.execute('update Turnos set Clinica_ID=?, Profesional_Matricula=?, Cod_Paciente=?, Practica_ID=?, Fecha_Reserva=?, Fecha_Turno=?, Notificado=?, Cancelado=?, Finalizado=?, Titulo=?, Descripcion=? where id=?', (clinicID, professionalID, codClient, practiceID, reservationDate, appointmentDay, notified, cancelled, finalized, title, description,appointmentID))

        rowCount = c.rowcount
        conn.commit()
        if rowCount == 0:   #Si no se afecto ninguna fila, es porque el itemid no existe.
            return {"error": 1, "status": "El turno " + str(appointmentID) + " no existe."}
        else:
            return {"error": 0, "status": "Success"}
    except Exception as e:
        print('Error: ', e)
        return {"error": 2, "status": e}

def get_all_items():
    try:
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute('select * from items')
        rows = c.fetchall()

        """
        rowarray_list = []

        for row in rows:
            t = (row[0], row[1], row[2])
            rowarray_list.append(t)

        respuesta = {"items" : rowarray_list}
        j = json.dumps(respuesta)
        """

        objects_list = []
        
        for row in rows:
            d = collections.OrderedDict()
            d['id'] = row[0]
            d['item'] = row[1]
            d['status'] = row[2]
            objects_list.append(d)

        respuesta = {"items" : objects_list}
        #j = json.dumps(respuesta)

        return respuesta
    except Exception as e:
        print('Error: ', e)
        return None





def delete_item(itemid):
    try:
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute('delete from items where id=?', (itemid,))
        rowCount = c.rowcount
        conn.commit()
        if rowCount == 0:
            return {"error" : "El item " + itemid + " no existe."}
        else:
            return {"Item eliminado": itemid}
    except Exception as e:
        print('Error: ', e)
        return None