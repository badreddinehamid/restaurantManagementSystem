from connectionDB import DBconnector


class Manipulation :
    def __init__(self,database) -> None:
        self._database = database


    
    def saveReservation(self, num_table):
        self._database.connect_to_db()
        query = f"insert into reservation (id,num_table) values (1,{num_table});"
        print(query)
        self._database.execute_query(query)
        self._database.close_DB()
        print("reservation saved...")

class Show:
    def __init__(self,database) -> None:
        self._database = database

    
    def show_reservations(self):
        self._database.connect_to_db()
        query = "select * from reservation;"
        reservation_result = self._database.read_query(query)
        return reservation_result
     



managerConnnector = DBconnector('localhost','restaurantManager',"password","restaurantManangementDB")
insertionController = Manipulation(managerConnnector)
insertionController.saveReservation(5)

showController = Show(managerConnnector)
print(showController.show_reservations())