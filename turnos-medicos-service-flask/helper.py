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
            return {"error": 1, "status": 'There are no events'}
            
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
        return {"error": 0, "status": objects_list}
    except Exception as e:
        print('Error: ', str(e))
        return {"error": 2, "status": str(e)}

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
        print('Error: ', str(e))
        return {"error": 1, "status": str(e)}

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
        print('Error: ', str(e))
        return {"error": 2, "status": str(e)}






def get_professional_events(clinicID,professionalID):
    try:
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute("select * from Turnos where Clinica_ID=? AND Profesional_Matricula=?", (clinicID,professionalID))
        rows = c.fetchall()
        rowCount = len(rows)
        conn.commit()

        if rowCount == 0:
            return {"error": 1, "status": "There are no events"}
            
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
        return {"error": 0, "status": objects_list}
    except Exception as e:
        print('Error: ', str(e))
        return {"error": 0, "status": str(e)}





def get_professional_day_events(data):
    try:
        clinicID = data[0]
        professionalID = data[1]
        beginDate = data[2]
        finishDate = data[3]

        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        
        c.execute('select * from Turnos where Clinica_ID=? AND Profesional_Matricula=? AND Fecha_Turno <= ? AND Fecha_Turno >= ?',(clinicID,professionalID,finishDate,beginDate))

        rows = c.fetchall()
        rowCount = len(rows)
        conn.commit()
        if rowCount == 0:
            {"error": 1, "status":"There are no events"}
            
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
        return {"error": 0, "status": objects_list}
    except Exception as e:
        print('Error: ', str(e))
        return {"error": 2, "status": str(e)}





def get_professional_schedule(clinicID,professionalID):
    try:
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute("select * from Horarios where Clinica_ID=? AND Profesional_Matricula=?", (clinicID,professionalID))
        rows = c.fetchall()
        rowCount = len(rows)
        conn.commit()

        if rowCount == 0:
            return {"error": 1, "status": "There are no Schedule for this professional"}
            
        objects_list = []
        for row in rows:
            d = collections.OrderedDict()
            d['Dia'] = row[3]
            d['Horario_Inicio'] = row[4]
            d['Horario_Fin'] = row[5]
            objects_list.append(d)
        return {"error": 0, "status": objects_list}
    except Exception as e:
        print('Error: ', str(e))
        return {"error": 2, "status": str(e)}


def get_professional_day_schedule(data):
    try:
        clinicID = data[0]
        professionalID = data[1]
        date = data[2]

        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        
        c.execute('select * from Horarios where Clinica_ID=? AND Profesional_Matricula=? AND Dia = ?',(clinicID,professionalID,date))

        rows = c.fetchall()
        rowCount = len(rows)
        conn.commit()
        if rowCount == 0:
            return {"error": 1, "status": "There are no Schedule for this professional in this day"}
            
        objects_list = []
        for row in rows:
            d = collections.OrderedDict()
            d['Dia'] = row[3]
            d['Horario_Inicio'] = row[4]
            d['Horario_Fin'] = row[5]
            objects_list.append(d)
        return {"error": 0, "status": objects_list}
    except Exception as e:
        print('Error: ', str(e))
        return {"error": 2, "status": str(e)}

