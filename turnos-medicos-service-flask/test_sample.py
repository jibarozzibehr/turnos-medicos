import helper
import json

def func(x):
    return x + 1


def test_add_Well():
    clinicID = 1
    professionalID = "123456"
    codClient = 1
    practiceID = 1
    reservationDate = "2020-12-18 18:59"
    appointmentDay = "2020-12-26 16:00"
    notified = 0
    cancelled = 0
    finalized = 0
    
    title = "Esto es una prueba"
    description = "Prueba" 

    data = [clinicID,professionalID,codClient,practiceID,reservationDate,appointmentDay,notified,cancelled,finalized,title,description]
    assert json.loads(json.dumps(helper.add_event(data)))["error"] == 0


def test_add_Bad():
    clinicID = None
    professionalID = "123456"
    codClient = 1
    practiceID = 1
    reservationDate = "2020-12-18 18:59"
    appointmentDay = "2020-12-26 16:00"
    notified = 0
    cancelled = 0
    finalized = 0
    
    title = "Esto es una prueba"
    description = "Prueba" 

    data = [clinicID,professionalID,codClient,practiceID,reservationDate,appointmentDay,notified,cancelled,finalized,title,description]
    assert json.loads(json.dumps(helper.add_event(data)))["error"] == 3


def test_getClientEvents_Well():

    clientID = 2

    assert json.loads(json.dumps(helper.get_client_events(clientID)))["error"] == 0


def test_getClientEvents_Bad():

    clientID = 5

    assert json.loads(json.dumps(helper.get_client_events(clientID)))["error"] == 1



def test_update_event_Well():

    appointmentID = 1
    clinicID = 1
    professionalID = "123456"
    codClient = 1
    practiceID = 1
    reservationDate = "2020-11-27 14:59"
    appointmentDay = "2020-11-24 12:00"
    notified = 0
    cancelled = 0
    finalized = 0
    
    title = "Limprieza para los dientes"
    description = "Estan muy sucios"

    data = [appointmentID, clinicID,professionalID,codClient,practiceID,reservationDate,appointmentDay,notified,cancelled,finalized,title,description]

    assert json.loads(json.dumps(helper.update_event(data)))["error"] == 0



def test_update_event_Bad():

    appointmentID = 250
    clinicID = 1
    professionalID = "123456"
    codClient = 1
    practiceID = 1
    reservationDate = "2020-11-27 14:59"
    appointmentDay = "2020-11-24 12:00"
    notified = 0
    cancelled = 0
    finalized = 0
    
    title = "Limprieza para los dientes"
    description = "Estan muy sucios"

    data = [appointmentID, clinicID,professionalID,codClient,practiceID,reservationDate,appointmentDay,notified,cancelled,finalized,title,description]

    assert json.loads(json.dumps(helper.update_event(data)))["error"] == 1




def test_delete_event_Well():

    appointmentID = 1

    data = [appointmentID]

    assert json.loads(json.dumps(helper.delete_event(data)))["error"] == 0



def test_delete_event_Bad():

    appointmentID = 125

    data = [appointmentID]

    assert json.loads(json.dumps(helper.delete_event(data)))["error"] == 1


def test_notify_event_Well():

    appointmentID = 1

    data = [appointmentID]

    assert json.loads(json.dumps(helper.notify_event(data)))["error"] == 0



def test_notify_event_Bad():

    appointmentID = 125

    data = [appointmentID]

    assert json.loads(json.dumps(helper.notify_event(data)))["error"] == 1
    

def test_finalize_event_Well():

    appointmentID = 1

    data = [appointmentID]

    assert json.loads(json.dumps(helper.finalize_event(data)))["error"] == 0



def test_finalize_event_Bad():

    appointmentID = 125

    data = [appointmentID]

    assert json.loads(json.dumps(helper.finalize_event(data)))["error"] == 1



def test_get_professional_events_Well():

    professionalID = "1"

    assert json.loads(json.dumps(helper.get_professional_events(professionalID)))["error"] == 0


def test_get_professional_events_Bad():

    professionalID = "12"

    assert json.loads(json.dumps(helper.get_professional_events(professionalID)))["error"] == 1



def test_get_professional_events_byClinic_Well():

    clinicID = 1
    professionalID = "1"

    assert json.loads(json.dumps(helper.get_professional_events_byClinic(clinicID,professionalID)))["error"] == 0


def test_get_professional_events_byClinic_Bad():

    clinicID = 1
    professionalID = "12"

    assert json.loads(json.dumps(helper.get_professional_events_byClinic(clinicID,professionalID)))["error"] == 1


def test_get_professional_events_byClinic_Bad2():

    clinicID = 12
    professionalID = "1"

    assert json.loads(json.dumps(helper.get_professional_events_byClinic(clinicID,professionalID)))["error"] == 1




def test_get_professional_events_not_cancelled_Well():

    clinicID = 1
    professionalID = "1"

    assert json.loads(json.dumps(helper.get_professional_events_not_cancelled(clinicID,professionalID)))["error"] == 0


def test_get_professional_events_not_cancelled_Bad():

    clinicID = 1
    professionalID = "12"

    assert json.loads(json.dumps(helper.get_professional_events_not_cancelled(clinicID,professionalID)))["error"] == 1


def test_get_professional_events_not_cancelled_Bad2():

    clinicID = 12
    professionalID = "1"

    assert json.loads(json.dumps(helper.get_professional_events_not_cancelled(clinicID,professionalID)))["error"] == 1



def test_get_client_events_Well():

    clientID = 2

    assert json.loads(json.dumps(helper.get_client_events(clientID)))["error"] == 0


def test_get_client_events_Bad():

    clientID = 12

    assert json.loads(json.dumps(helper.get_client_events(clientID)))["error"] == 1



