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
    except Exception as e:
        print('Error: ', str(e))
        return {"error": 2, "status": str(e)}

    try:
        c = conn.cursor()
    except Exception as e:
        print('Error: ', str(e))
        return {"error": 3, "status": str(e)}


    try:
        c.execute("select * from Turnos where Cod_Paciente=%s" % clientID)
    except Exception as e:
        print('Error: ', str(e))
        return {"error": 4, "status": str(e)}

    try:
        rows = c.fetchall()
    except Exception as e:
        print('Error: ', str(e))
        return {"error": 5, "status": str(e)}


    rowCount = len(rows)

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
    

def add_event(data):
    
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

    try:
        conn = sqlite3.connect(DB_PATH)
    except Exception as e:
        print('Error: ', str(e))
        return {"error": 1, "status": str(e)}

    # Once a connection has been established, we use the cursor
    # object to execute queries
    try:
        c = conn.cursor()
    except Exception as e:
        print('Error: ', str(e))
        return {"error": 2, "status": str(e)}

    # Keep the initial status as Not Started
    # c.execute('insert into items(item, status) values(?,?)', (item, NOTSTARTED))
    try:
        c.execute('insert into Turnos (Clinica_ID, Profesional_Matricula, Cod_Paciente, Practica_ID, Fecha_Reserva, Fecha_Turno, Notificado, Cancelado, Finalizado, Titulo, Descripcion) values(?,?,?,?,?,?,?,?,?,?,?)', (clinicID, professionalID, codClient, practiceID, reservationDate, appointmentDay, notified, cancelled, finalized, title, description))
    except Exception as e:
        print('Error: ', str(e))
        return {"error": 3, "status": str(e)}

    # We commit to save the change
    conn.commit()
    return {"error": 0, "status": 'Success'}



def update_event(data):
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

    try:
        conn = sqlite3.connect(DB_PATH)
    except Exception as e:
        print('Error: ', str(e))
        return {"error": 2, "status": str(e)}

    try:
        c = conn.cursor()
    except Exception as e:
        print('Error: ', str(e))
        return {"error": 3, "status": str(e)}

    try:
        c.execute('update Turnos set Clinica_ID=?, Profesional_Matricula=?, Cod_Paciente=?, Practica_ID=?, Fecha_Reserva=?, Fecha_Turno=?, Notificado=?, Cancelado=?, Finalizado=?, Titulo=?, Descripcion=? where id=?', (clinicID, professionalID, codClient, practiceID, reservationDate, appointmentDay, notified, cancelled, finalized, title, description,appointmentID))
    except Exception as e:
        print('Error: ', str(e))
        return {"error": 4, "status": str(e)}

    rowCount = c.rowcount


    try:
        conn.commit()
    except Exception as e:
        print('Error: ', str(e))
        return {"error": 5, "status": str(e)}


    if rowCount == 0:   #Si no se afecto ninguna fila, es porque el itemid no existe.
        return {"error": 1, "status": "El turno " + str(appointmentID) + " no existe."}
    else:
        return {"error": 0, "status": "Success"}

def delete_event(data):
    appointmentID = data[0]
    print("Hola buenas tardes")
    print(data)
    print(appointmentID)

    try:
        conn = sqlite3.connect(DB_PATH)
    except Exception as e:
        print('Error: ', str(e))
        return {"error": 5, "status": str(e)}

    try:
        c = conn.cursor()
    except Exception as e:
        print('Error: ', str(e))
        return {"error": 4, "status": str(e)}

    try:
        c.execute('update Turnos set Cancelado=1 where id=?', (appointmentID,))
    except Exception as e:
        print('Error: ', str(e))
        return {"error": 3, "status": str(e)}


    rowCount = c.rowcount

    try:
        conn.commit()
    except Exception as e:
        print('Error: ', str(e))
        return {"error": 2, "status": str(e)}


    if rowCount == 0:   #Si no se afecto ninguna fila, es porque el itemid no existe.
        return {"error": 1, "status": "El turno " + str(appointmentID) + " no existe."}
    else:
        return {"error": 0, "status": "Success"}
    

def notify_event(data):
    
    appointmentID = data[0]

    try:
        conn = sqlite3.connect(DB_PATH)
    except Exception as e:
        print('Error: ', str(e))
        return {"error": 5, "status": str(e)}

        
    try:
        c = conn.cursor()
    except Exception as e:
        print('Error: ', str(e))
        return {"error": 4, "status": str(e)}

        
    try:
        c.execute('update Turnos set Notificado=1 where id=?', (appointmentID,))
    except Exception as e:
        print('Error: ', str(e))
        return {"error": 3, "status": str(e)}


    rowCount = c.rowcount
    
    try:
        conn.commit()
    except Exception as e:
        print('Error: ', str(e))
        return {"error": 2, "status": str(e)}

    

    if rowCount == 0:   #Si no se afecto ninguna fila, es porque el itemid no existe.
        return {"error": 1, "status": "El turno " + str(appointmentID) + " no existe."}
    else:
        return {"error": 0, "status": "Success"}
    

def finalize_event(data):
    
    appointmentID = data[0]

    try:
        conn = sqlite3.connect(DB_PATH)
    except Exception as e:
        print('Error: ', str(e))
        return {"error": 5, "status": str(e)}


    try:
        c = conn.cursor()
    except Exception as e:
        print('Error: ', str(e))
        return {"error": 4, "status": str(e)}


    try:
        c.execute('update Turnos set Finalizado=1 where id=?', (appointmentID,))
    except Exception as e:
        print('Error: ', str(e))
        return {"error": 3, "status": str(e)}


    rowCount = c.rowcount
    
    try:
        conn.commit()
    except Exception as e:
        print('Error: ', str(e))
        return {"error": 2, "status": str(e)}

    

    if rowCount == 0:   #Si no se afecto ninguna fila, es porque el itemid no existe.
        return {"error": 1, "status": "El turno " + str(appointmentID) + " no existe."}
    else:
        return {"error": 0, "status": "Success"}
    





def get_professional_events(professionalID):
    try:    
        conn = sqlite3.connect(DB_PATH)
    except Exception as e:
        print('Error: ', str(e))
        return {"error": 5, "status": str(e)}


    try:
        c = conn.cursor()
    except Exception as e:
        print('Error: ', str(e))
        return {"error": 4, "status": str(e)}


    try:
        c.execute("select Turnos.ID, Turnos.Clinica_ID, Turnos.Profesional_Matricula, Turnos.Cod_Paciente, Turnos.Practica_ID, Turnos.Fecha_Reserva, Turnos.Fecha_Turno, Turnos.Notificado, Turnos.Cancelado, Turnos.Finalizado, Turnos.Titulo, Turnos.Descripcion, Usuarios.Nombre, Clinicas.Nombre from Turnos, Pacientes, Usuarios, Clinicas where Turnos.Profesional_Matricula=? AND Turnos.Cancelado = 0 AND Turnos.Finalizado = 0 AND Turnos.Fecha_Turno >= datetime('now', 'localtime') AND Turnos.Cod_Paciente = Pacientes.Cod_Paciente AND Turnos.Clinica_ID = Clinicas.ID AND Pacientes.Usuario_ID = Usuarios.ID order by Turnos.Fecha_Turno asc", (professionalID,))
    except Exception as e:
        print('Error: ', str(e))
        return {"error": 3, "status": str(e)}

        
    try:
        rows = c.fetchall()
    except Exception as e:
        print('Error: ', str(e))
        return {"error": 2, "status": str(e)}



    rowCount = len(rows)

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
        
        d['Paciente'] = row[12]
        d['Clinica'] = row[13]
        objects_list.append(d)
    return {"error": 0, "status": objects_list}
    




def get_professional_events_byClinic(clinicID,professionalID):
    try:
        conn = sqlite3.connect(DB_PATH)
    except Exception as e:
        print('Error: ', str(e))
        return {"error": 5, "status": str(e)}


    try:
        c = conn.cursor()
    except Exception as e:
        print('Error: ', str(e))
        return {"error": 4, "status": str(e)}


    try:
        c.execute("select * from Turnos where Clinica_ID=? AND Profesional_Matricula=? order by Turnos.Fecha_Turno asc", (clinicID, professionalID))
    except Exception as e:
        print('Error: ', str(e))
        return {"error": 3, "status": str(e)}


    try:
        rows = c.fetchall()
    except Exception as e:
        print('Error: ', str(e))
        return {"error": 2, "status": str(e)}


    rowCount = len(rows)

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
    


def get_professional_events_not_cancelled(clinicID,professionalID):
    try:
        conn = sqlite3.connect(DB_PATH)
    except Exception as e:
        print('Error: ', str(e))
        return {"error": 5, "status": str(e)}


    try:
        c = conn.cursor()
    except Exception as e:
        print('Error: ', str(e))
        return {"error": 4, "status": str(e)}


    try:
        c.execute("select * from Turnos where Clinica_ID=? AND Profesional_Matricula=? AND Cancelado=0 AND Finalizado=0 AND Fecha_Turno >= datetime('now', 'localtime') order by Turnos.Fecha_Turno asc", (clinicID, professionalID))
    except Exception as e:
        print('Error: ', str(e))
        return {"error": 3, "status": str(e)}


    try:
        rows = c.fetchall()
    except Exception as e:
        print('Error: ', str(e))
        return {"error": 2, "status": str(e)}



    rowCount = len(rows)

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
    





def get_professional_day_events(data):
    
    clinicID = data[0]
    professionalID = data[1]
    beginDate = data[2]
    finishDate = data[3]

    try:
        conn = sqlite3.connect(DB_PATH)
    except Exception as e:
        print('Error: ', str(e))
        return {"error": 5, "status": str(e)}


    try:
        c = conn.cursor()
    except Exception as e:
        print('Error: ', str(e))
        return {"error": 4, "status": str(e)}


    try:
        c.execute('select * from Turnos where Cancelado = 0 AND Finalizado = 0 AND Clinica_ID=? AND Profesional_Matricula=? AND Fecha_Turno <= ? AND Fecha_Turno >= ? Order by Fecha_Turno',(clinicID,professionalID,finishDate,beginDate))
    except Exception as e:
        print('Error: ', str(e))
        return {"error": 3, "status": str(e)}


    try:
        rows = c.fetchall()
    except Exception as e:
        print('Error: ', str(e))
        return {"error": 2, "status": str(e)}


    rowCount = len(rows)

    if rowCount == 0:
        return {"error": 1, "status":"There are no events"}
        
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
    





def get_professional_schedule(clinicID,professionalID):
    try:
        conn = sqlite3.connect(DB_PATH)
    except Exception as e:
        print('Error: ', str(e))
        return {"error": 5, "status": str(e)}


    try:
        c = conn.cursor()
    except Exception as e:
        print('Error: ', str(e))
        return {"error": 4, "status": str(e)}


    try:
        c.execute("select * from Horarios where Clinica_ID=? AND Profesional_Matricula=?", (clinicID,professionalID))
    except Exception as e:
        print('Error: ', str(e))
        return {"error": 3, "status": str(e)}


    try:
        rows = c.fetchall()
    except Exception as e:
        print('Error: ', str(e))
        return {"error": 2, "status": str(e)}


    rowCount = len(rows)

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
    


def get_professional_day_schedule(data):

    clinicID = data[0]
    professionalID = data[1]
    date = data[2]

    try:
        conn = sqlite3.connect(DB_PATH)
    except Exception as e:
        print('Error: ', str(e))
        return {"error": 5, "status": str(e)}


    try:
        c = conn.cursor()
    except Exception as e:
        print('Error: ', str(e))
        return {"error": 4, "status": str(e)}


    try:        
        c.execute('select * from Horarios where Clinica_ID=? AND Profesional_Matricula=? AND Dia = ?',(clinicID,professionalID,date))
    except Exception as e:
        print('Error: ', str(e))
        return {"error": 3, "status": str(e)}


    try:
        rows = c.fetchall()
    except Exception as e:
        print('Error: ', str(e))
        return {"error": 2, "status": str(e)}


    rowCount = len(rows)

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
    


def get_client_pending_events(clientID):
    try:
        conn = sqlite3.connect(DB_PATH)
    except Exception as e:
        print('Error: ', str(e))
        return {"error": 5, "status": str(e)}


    try:
        c = conn.cursor()
    except Exception as e:
        print('Error: ', str(e))
        return {"error": 4, "status": str(e)}

        
    try:
        c.execute("select Turnos.ID, Turnos.Clinica_ID, Turnos.Profesional_Matricula, Turnos.Cod_Paciente, Turnos.Practica_ID, Turnos.Fecha_Reserva, Turnos.Fecha_Turno, Turnos.Notificado, Turnos.Cancelado, Turnos.Finalizado, Turnos.Titulo, Turnos.Descripcion, Usuarios.Nombre, Clinicas.Nombre from Turnos, Profesionales, Usuarios, Clinicas where Turnos.Cod_Paciente=? AND Turnos.Cancelado = 0 AND Turnos.Finalizado = 0 AND Turnos.Fecha_Turno >= datetime('now', '-1 hour', 'localtime') AND Turnos.Profesional_Matricula = Profesionales.Matricula AND Turnos.Clinica_ID = Clinicas.ID AND Profesionales.Usuario_ID = Usuarios.ID ORDER BY Turnos.Fecha_Turno asc;", (clientID,))
    except Exception as e:
        print('Error: ', str(e))
        return {"error": 3, "status": str(e)}

        
    try:
        rows = c.fetchall()
    except Exception as e:
        print('Error: ', str(e))
        return {"error": 2, "status": str(e)}

    

    rowCount = len(rows)

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
    

def get_specialities():
    try:
        conn = sqlite3.connect(DB_PATH)
    except Exception as e:
        print('Error: ', str(e))
        return {"error": 5, "status": str(e)}


    try:
        c = conn.cursor()
    except Exception as e:
        print('Error: ', str(e))
        return {"error": 4, "status": str(e)}


    try:
        c.execute("select * from Especialidades")
    except Exception as e:
        print('Error: ', str(e))
        return {"error": 3, "status": str(e)}


    try:
        rows = c.fetchall()
    except Exception as e:
        print('Error: ', str(e))
        return {"error": 2, "status": str(e)}


    rowCount = len(rows)

    if rowCount == 0:
        return {"error": 1, "status": "There are no specialities."}
        
    objects_list = []
    for row in rows:
        d = collections.OrderedDict()
        d['ID'] = row[0]
        d['Nombre'] = row[1]
        objects_list.append(d)
    return {"error": 0, "status": objects_list}
    
        
def get_practices():
    try:
        conn = sqlite3.connect(DB_PATH)
    except Exception as e:
        print('Error: ', str(e))
        return {"error": 5, "status": str(e)}


    try:
        c = conn.cursor()
    except Exception as e:
        print('Error: ', str(e))
        return {"error": 4, "status": str(e)}


    try:
        c.execute("select * from Practicas")
    except Exception as e:
        print('Error: ', str(e))
        return {"error": 3, "status": str(e)}


    try:
        rows = c.fetchall()
    except Exception as e:
        print('Error: ', str(e))
        return {"error": 2, "status": str(e)}


    rowCount = len(rows)

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
    



def get_practices_by_specialities(specialityID):
    try:
        conn = sqlite3.connect(DB_PATH)
    except Exception as e:
        print('Error: ', str(e))
        return {"error": 5, "status": str(e)}


    try:
        c = conn.cursor()
    except Exception as e:
        print('Error: ', str(e))
        return {"error": 4, "status": str(e)}


    try:
        c.execute("select * from Practicas where Especialidad_ID=?", (specialityID,))
    except Exception as e:
        print('Error: ', str(e))
        return {"error": 3, "status": str(e)}


    try:
        rows = c.fetchall()
    except Exception as e:
        print('Error: ', str(e))
        return {"error": 2, "status": str(e)}


    rowCount = len(rows)

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
    

def get_professionals():
    try:
        conn = sqlite3.connect(DB_PATH)
    except Exception as e:
        print('Error: ', str(e))
        return {"error": 5, "status": str(e)}


    try:
        c = conn.cursor()
    except Exception as e:
        print('Error: ', str(e))
        return {"error": 4, "status": str(e)}


    try:
        c.execute("select Profesionales.Matricula, Profesionales.Especialidad_ID, Profesionales.Activo, Usuarios.Nombre, Usuarios.DNI, Usuarios.Telefono, Usuarios.Email from Profesionales, Usuarios where Profesionales.Usuario_ID = Usuarios.ID")
    except Exception as e:
        print('Error: ', str(e))
        return {"error": 3, "status": str(e)}


    try:
        rows = c.fetchall()
    except Exception as e:
        print('Error: ', str(e))
        return {"error": 2, "status": str(e)}

    
    rowCount = len(rows)

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
    




def get_clients():
    try:
        conn = sqlite3.connect(DB_PATH)
    except Exception as e:
        print('Error: ', str(e))
        return {"error": 5, "status": str(e)}


    try:
        c = conn.cursor()
    except Exception as e:
        print('Error: ', str(e))
        return {"error": 4, "status": str(e)}


    try:
        c.execute("select Pacientes.Cod_Paciente, Pacientes.Usuario_ID, Usuarios.Nombre, Usuarios.DNI, Usuarios.Telefono, Usuarios.Email from Pacientes, Usuarios where Pacientes.Usuario_ID = Usuarios.ID")
    except Exception as e:
        print('Error: ', str(e))
        return {"error": 3, "status": str(e)}


    try:
        rows = c.fetchall()
    except Exception as e:
        print('Error: ', str(e))
        return {"error": 2, "status": str(e)}


    rowCount = len(rows)

    if rowCount == 0:
        return {"error": 1, "status": "There are no clients."}
        
    objects_list = []
    for row in rows:
        d = collections.OrderedDict()
        d['Cod_Paciente'] = row[0]
        d['Usuario_ID'] = row[1]
        d['Nombre'] = row[2]
        d['DNI'] = row[3]
        d['Telefono'] = row[4]
        d['Email'] = row[5]
        objects_list.append(d)
    return {"error": 0, "status": objects_list}
    



def get_professionals_by_specialities(specialityID):
    try:
        conn = sqlite3.connect(DB_PATH)
    except Exception as e:
        print('Error: ', str(e))
        return {"error": 5, "status": str(e)}


    try:
        c = conn.cursor()
    except Exception as e:
        print('Error: ', str(e))
        return {"error": 4, "status": str(e)}


    try:
        c.execute("select Profesionales.Matricula, Profesionales.Especialidad_ID, Profesionales.Activo, Usuarios.Nombre, Usuarios.DNI, Usuarios.Telefono, Usuarios.Email from Profesionales, Usuarios where Profesionales.Usuario_ID = Usuarios.ID AND Profesionales.Especialidad_ID=?", (specialityID,))
    except Exception as e:
        print('Error: ', str(e))
        return {"error": 3, "status": str(e)}


    try:
        rows = c.fetchall()
    except Exception as e:
        print('Error: ', str(e))
        return {"error": 2, "status": str(e)}


    rowCount = len(rows)

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
    



def get_clinics():
    print('Hola')
    try:
        
        conn = sqlite3.connect(DB_PATH)
    except Exception as e:
        print('Error: ', str(e))
        return {"error": 5, "status": str(e)}


    try:
        c = conn.cursor()
    except Exception as e:
        print('Error: ', str(e))
        return {"error": 4, "status": str(e)}


    try:
        c.execute("select * from Clinicas")
    except Exception as e:
        print('Error: ', str(e))
        return {"error": 3, "status": str(e)}


    try:
        rows = c.fetchall()
    except Exception as e:
        print('Error: ', str(e))
        return {"error": 2, "status": str(e)}


    rowCount = len(rows)

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
    

def get_professionals_clinics(professionalID):
    try:
        conn = sqlite3.connect(DB_PATH)
    except Exception as e:
        print('Error: ', str(e))
        return {"error": 5, "status": str(e)}


    try:
        c = conn.cursor()
    except Exception as e:
        print('Error: ', str(e))
        return {"error": 4, "status": str(e)}


    try:
        c.execute("select Clinicas.ID, Clinicas.Nombre from Clinicas, Clinicas_Profesionales where Clinicas_Profesionales.Profesional_Matricula = ? and Clinicas_Profesionales.Clinica_ID = Clinicas.ID", (professionalID,))
    except Exception as e:
        print('Error: ', str(e))
        return {"error": 3, "status": str(e)}


    try:
        rows = c.fetchall()
    except Exception as e:
        print('Error: ', str(e))
        return {"error": 2, "status": str(e)}


    rowCount = len(rows)

    if rowCount == 0:
        return {"error": 1, "status": "There are no clinics for that doctor."}
        
    objects_list = []
    for row in rows:
        d = collections.OrderedDict()
        d['ID'] = row[0]
        d['Nombre'] = row[1]
        objects_list.append(d)
    return {"error": 0, "status": objects_list}
    


def login(email, password):
    try:
        conn = sqlite3.connect(DB_PATH)
    except Exception as e:
        print('Error: ', str(e))
        return {"error": 5, "status": str(e)}


    try:
        c = conn.cursor()
    except Exception as e:
        print('Error: ', str(e))
        return {"error": 4, "status": str(e)}


    try:
        c.execute("select ID from Usuarios where Email=? COLLATE NOCASE and Contraseña=? ", (email, password))
    except Exception as e:
        print('Error: ', str(e))
        return {"error": 3, "status": str(e)}


    try:
        rows = c.fetchall()
    except Exception as e:
        print('Error: ', str(e))
        return {"error": 2, "status": str(e)}


    rowCount = len(rows)

    if rowCount == 0:
        return {"error": 1, "status": "Email o contraseña incorrectos."}
        
    objects_list = []
    for row in rows:
        d = collections.OrderedDict()
        d['ID'] = row[0]
        objects_list.append(d)
    return {"error": 0, "status": objects_list}
    



def isProfessional(userID):
    try:
        conn = sqlite3.connect(DB_PATH)
    except Exception as e:
        print('Error: ', str(e))
        return {"error": 4, "status": str(e)}


    try:
        c = conn.cursor()
    except Exception as e:
        print('Error: ', str(e))
        return {"error": 3, "status": str(e)}


    try:
        c.execute("select Matricula, Especialidad_ID from Profesionales where Usuario_ID=?", (userID,))
    except Exception as e:
        print('Error: ', str(e))
        return {"error": 2, "status": str(e)}


    try:
        rows = c.fetchall()
    except Exception as e:
        print('Error: ', str(e))
        return {"error": 1, "status": str(e)}


    rowCount = len(rows)

    if rowCount == 0:
        return {"error": 0, "status": {"isProfessional": False, "matricula": -1, "especialidadID": -1}}
        
    '''objects_list = []
    for row in rows:
        d = collections.OrderedDict()
        d['isProfessional'] = True
        objects_list.append(d)'''
    
    # d = collections.OrderedDict()
    # d['Matricula'] = rows[0]
    # d['Especialidad_ID'] = rows[1]

    matricula = rows[0][0]
    especialidadID = rows[0][1]

    return { "error": 0, "status": {"isProfessional": True, "matricula": matricula, "especialidadID": especialidadID}}

    

def isClient(userID):
    try:
        conn = sqlite3.connect(DB_PATH)
    except Exception as e:
        print('Error: ', str(e))
        return {"error": 4, "status": str(e)}


    try:
        c = conn.cursor()
    except Exception as e:
        print('Error: ', str(e))
        return {"error": 3, "status": str(e)}


    try:
        c.execute("select Cod_Paciente from Pacientes where Usuario_ID=?", (userID,))
    except Exception as e:
        print('Error: ', str(e))
        return {"error": 2, "status": str(e)}


    try:
        rows = c.fetchall()
    except Exception as e:
        print('Error: ', str(e))
        return {"error": 1, "status": str(e)}


    rowCount = len(rows)

    if rowCount == 0:
        return {"error": 0, "status": {"isClient": False, "codPaciente": -1}}
        
    '''objects_list = []
    for row in rows:
        d = collections.OrderedDict()
        d['isProfessional'] = True
        objects_list.append(d)'''
    
    #d = collections.OrderedDict()
    #d['Matricula'] = rows[0]

    codPaciente = rows[0][0]

    return { "error": 0, "status": {"isClient": True, "codPaciente": codPaciente }}

    

def get_user_data(userID):
    try:
        conn = sqlite3.connect(DB_PATH)
    except Exception as e:
        print('Error: ', str(e))
        return {"error": 5, "status": str(e)}


    try:
        c = conn.cursor()
    except Exception as e:
        print('Error: ', str(e))
        return {"error": 4, "status": str(e)}


    try:
        c.execute("select * from Usuarios where ID=?", (userID,))
    except Exception as e:
        print('Error: ', str(e))
        return {"error": 3, "status": str(e)}


    try:
        rows = c.fetchall()
    except Exception as e:
        print('Error: ', str(e))
        return {"error": 2, "status": str(e)}


    rowCount = len(rows)
    

    if rowCount == 0:
        return {"error": 1, "status": "The user with ID " + str(userID) + " doesn't exist."}
        
    '''objects_list = []
    for row in rows:
        d = collections.OrderedDict()
        d['isProfessional'] = True
        objects_list.append(d)'''
    
    data = []

    d = collections.OrderedDict()

    d['email'] = rows[0][1]
    d['nombre'] = rows[0][3]
    d['dni'] = rows[0][4]
    d['telefono'] = rows[0][5]

    data.append(d)

    return { "error": 0, "status": d }

    

def edit_user(data):
    
    userID = data[0]
    nombre = data[1]
    dni = data[2]
    email = data[3]
    telefono = data[4]

    try:
        conn = sqlite3.connect(DB_PATH)
    except Exception as e:
        print('Error: ', str(e))
        return {"error": 5, "status": str(e)}


    try:
        c = conn.cursor()
    except Exception as e:
        print('Error: ', str(e))
        return {"error": 4, "status": str(e)}


    try:
        c.execute('update Usuarios set Email=?, Nombre=?, DNI=?, Telefono=? where id=?', (email, nombre, dni, telefono, userID))
    except Exception as e:
        print('Error: ', str(e))
        return {"error": 3, "status": str(e)}

        

    rowCount = c.rowcount

    try:
        conn.commit()
    except Exception as e:
        print('Error: ', str(e))
        return {"error": 2, "status": str(e)}


    if rowCount == 0:   #Si no se afecto ninguna fila, es porque el usuario no existe.
        return {"error": 1, "status": "El usuario con ID " + str(userID) + " no existe."}
    else:
        return {"error": 0, "status": "Success"}
    