from FreeTAKServer.model.SpecificCoT.SendTakPong import SendTakPong
from .SendCoTAbstractController import SendCoTAbstractController

from FreeTAKServer.controllers.configuration.LoggingConstants import LoggingConstants
from FreeTAKServer.controllers.CreateLoggerController import CreateLoggerController

loggingConstants = LoggingConstants()
logger = CreateLoggerController("SendInvalidCoTController").getLogger()
class SendPingController(SendCoTAbstractController):
    def __init__(self, RawCoT):
        try:
            RawCoT.xmlString = b'<event/>'
            tempObject = super().Event.takPong()
            object = SendTakPong()
            self.fill_object(object, tempObject, RawCoT, addToDB = False)
        except Exception as e:
            logger.error("there has been an exception in"
                         " the creation of a Ping model object " + str(e))