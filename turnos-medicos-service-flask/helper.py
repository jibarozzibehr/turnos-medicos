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

def delete_event(data):
    try:
        appointmentID = data[0]
        print("Hola buenas tardes")
        print(data)
        print(appointmentID)

        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()

        print(appointmentID)
        c.execute('update Turnos set Cancelado=1 where id=?', (str(appointmentID)))
        print(appointmentID)

        rowCount = c.rowcount
        conn.commit()
        if rowCount == 0:   #Si no se afecto ninguna fila, es porque el itemid no existe.
            return {"error": 1, "status": "El turno " + str(appointmentID) + " no existe."}
        else:
            return {"error": 0, "status": "Success"}
    except Exception as e:
        print('Error: ', str(e))
        return {"error": 2, "status": str(e)}

def notify_event(data):
    try:
        appointmentID = data[0]

        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        
        c.execute('update Turnos set Notificado=1 where id=?', (appointmentID))

        rowCount = c.rowcount
        conn.commit()
        if rowCount == 0:   #Si no se afecto ninguna fila, es porque el itemid no existe.
            return {"error": 1, "status": "El turno " + str(appointmentID) + " no existe."}
        else:
            return {"error": 0, "status": "Success"}
    except Exception as e:
        print('Error: ', str(e))
        return {"error": 2, "status": str(e)}

def finalize_event(data):
    try:
        appointmentID = data[0]

        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        
        c.execute('update Turnos set Finalizado=1 where id=?', (appointmentID))

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
        return {"error": 2, "status": str(e)}





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


def get_client_pending_events(clientID):
    try:
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute("select Turnos.ID, Turnos.Clinica_ID, Turnos.Profesional_Matricula, Turnos.Cod_Paciente, Turnos.Practica_ID, Turnos.Fecha_Reserva, Turnos.Fecha_Turno, Turnos.Notificado, Turnos.Cancelado, Turnos.Finalizado, Turnos.Titulo, Turnos.Descripcion, Usuarios.Nombre, Clinicas.Nombre from Turnos, Profesionales, Usuarios, Clinicas where Turnos.Cod_Paciente=? AND Turnos.Cancelado = 0 AND Turnos.Finalizado = 0 AND Turnos.Fecha_Turno >= datetime('now', '-1 hour', 'localtime') AND Turnos.Profesional_Matricula = Profesionales.Matricula AND Turnos.Clinica_ID = Clinicas.ID AND Profesionales.Usuario_ID = Usuarios.ID ORDER BY Turnos.Fecha_Turno asc;", (clientID))
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
            
            d['Profesional'] = row[12]
            d['Clinica'] = row[13]
            objects_list.append(d)
        return {"error": 0, "status": objects_list}
    except Exception as e:
        print('Error: ', str(e))
        return {"error": 2, "status": str(e)}

def get_specialities():
    try:
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute("select * from Especialidades")
        rows = c.fetchall()
        rowCount = len(rows)
        conn.commit()

        if rowCount == 0:
            return {"error": 1, "status": "There are no specialities."}
            
        objects_list = []
        for row in rows:
            d = collections.OrderedDict()
            d['ID'] = row[0]
            d['Nombre'] = row[1]
            objects_list.append(d)
        return {"error": 0, "status": objects_list}
    except Exception as e:
        print('Error: ', str(e))
        return {"error": 2, "status": str(e)}
        
def get_practices():
    try:
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute("select * from Practicas")
        rows = c.fetchall()
        rowCount = len(rows)
        conn.commit()

        if rowCount == 0:
            return {"error": 1, "status": "There are no practices."}
            
        objects_list = []
        for row in rows:
            d = collections.OrderedDict()
            d['ID'] = row[0]
            d['Nombre'] = row[1]
            d['Duracion_Turno'] = row[2]
            d['Especialidad_ID'] = row[3]
            objects_list.append(d)
        return {"error": 0, "status": objects_list}
    except Exception as e:
        print('Error: ', str(e))
        return {"error": 2, "status": str(e)}



def get_practices_by_specialities(specialityID):
    try:
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute("select * from Practicas where Especialidad_ID=?", (specialityID))
        rows = c.fetchall()
        rowCount = len(rows)
        conn.commit()

        if rowCount == 0:
            return {"error": 1, "status": "There are no practices for that speciality."}
            
        objects_list = []
        for row in rows:
            d = collections.OrderedDict()
            d['ID'] = row[0]
            d['Nombre'] = row[1]
            d['Duracion_Turno'] = row[2]
            d['Especialidad_ID'] = row[3]
            objects_list.append(d)
        return {"error": 0, "status": objects_list}
    except Exception as e:
        print('Error: ', str(e))
        return {"error": 2, "status": str(e)}

def get_professionals():
    try:
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute("select Profesionales.Matricula, Profesionales.Especialidad_ID, Profesionales.Activo, Usuarios.Nombre, Usuarios.DNI, Usuarios.Telefono, Usuarios.Email from Profesionales, Usuarios where Profesionales.Usuario_ID = Usuarios.ID")
        rows = c.fetchall()
        rowCount = len(rows)
        conn.commit()

        if rowCount == 0:
            return {"error": 1, "status": "There are no professionals."}
            
        objects_list = []
        for row in rows:
            d = collections.OrderedDict()
            d['Matricula'] = row[0]
            d['Especialidad_ID'] = row[1]
            d['Activo'] = row[2]
            d['Nombre'] = row[3]
            d['DNI'] = row[4]
            d['Telefono'] = row[5]
            d['Email'] = row[6]
            objects_list.append(d)
        return {"error": 0, "status": objects_list}
    except Exception as e:
        print('Error: ', str(e))
        return {"error": 2, "status": str(e)}

def get_professionals_by_specialities(specialityID):
    try:
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute("select Profesionales.Matricula, Profesionales.Especialidad_ID, Profesionales.Activo, Usuarios.Nombre, Usuarios.DNI, Usuarios.Telefono, Usuarios.Email from Profesionales, Usuarios where Profesionales.Usuario_ID = Usuarios.ID AND Profesionales.Especialidad_ID=?", (specialityID))
        rows = c.fetchall()
        rowCount = len(rows)
        conn.commit()

        if rowCount == 0:
            return {"error": 1, "status": "There are no professionals."}
            
        objects_list = []
        for row in rows:
            d = collections.OrderedDict()
            d['Matricula'] = row[0]
            d['Especialidad_ID'] = row[1]
            d['Activo'] = row[2]
            d['Nombre'] = row[3]
            d['DNI'] = row[4]
            d['Telefono'] = row[5]
            d['Email'] = row[6]
            objects_list.append(d)
        return {"error": 0, "status": objects_list}
    except Exception as e:
        print('Error: ', str(e))
        return {"error": 2, "status": str(e)}



def get_clinics():
    print('Hola')
    try:
        
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute("select * from Clinicas")
        rows = c.fetchall()
        rowCount = len(rows)
        conn.commit()

        if rowCount == 0:
            return {"error": 1, "status": "There are no clinics."}
            
        objects_list = []
        for row in rows:
            d = collections.OrderedDict()
            d['ID'] = row[0]
            d['Nombre'] = row[1]
            d['Direccion'] = row[2]
            d['Telefono'] = row[3]
            objects_list.append(d)
        return {"error": 0, "status": objects_list}
    except Exception as e:
        print('Error: ', str(e))
        return {"error": 2, "status": str(e)}


        