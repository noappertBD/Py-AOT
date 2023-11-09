import os
from sqlobject import (
    sqlhub,
    connectionForURI,
    SQLObject,
    StringCol,
    IntCol,
    DateTimeCol,
    ForeignKey,
    sqlbuilder,
)

db_filename = os.path.abspath("db/data.db")
connection_string = f"sqlite:{db_filename}"
sqlhub.processConnection = connectionForURI(connection_string)


class Users(SQLObject):
    server = IntCol()
    arrivedAt = StringCol()
    pseudo = StringCol()
    userId = IntCol()
    isMuted = StringCol()
    isThere = StringCol()
    isBanned = StringCol()
    warns = IntCol()
    kicks = IntCol()
    bans = IntCol()

    def toDict(self):
        return {
            "id": self.id,
            "server": self.server,
            "arrivedAt": self.arrivedAt,
            "pseudo": self.pseudo,
            "userId": self.userId,
            "isMuted": self.isMuted,
            "isThere": self.isThere,
            "isBanned": self.isBanned,
            "warns": self.warns,
            "kicks": self.kicks,
            "bans": self.bans,
        }


class Warns(SQLObject):
    server = IntCol()
    pseudo = StringCol()
    userId = StringCol()
    quantity = StringCol()
    reason = StringCol()

    def toDict(self):
        return {
            "id": self.id,
            "server": self.server,
            "pseudo": self.pseudo,
            "userId": self.userId,
            "quantity": self.quantity,
            "reason": self.reason,
        }


class Kicks(SQLObject):
    server = IntCol()
    pseudo = StringCol()
    userId = StringCol()
    reason = StringCol()

    def toDict(self):
        return {
            "id": self.id,
            "server": self.server,
            "pseudo": self.pseudo,
            "userId": self.userId,
            "reason": self.reason,
        }


class Bans(SQLObject):
    server = IntCol()
    pseudo = StringCol()
    userId = StringCol()
    reason = StringCol()
    until = DateTimeCol()

    def toDict(self):
        return {
            "id": self.id,
            "server": self.server,
            "pseudo": self.pseudo,
            "userId": self.userId,
            "reason": self.reason,
            "until": self.until,
        }


class Mutes(SQLObject):
    server = IntCol()
    pseudo = StringCol()
    userId = StringCol()
    reason = StringCol()
    until = DateTimeCol()

    def toDict(self):
        return {
            "id": self.id,
            "server": self.server,
            "pseudo": self.pseudo,
            "userId": self.userId,
            "reason": self.reason,
            "until": self.until,
        }


class RoomsLocker(SQLObject):
    server = IntCol()
    roomId = IntCol()
    locked = StringCol()

    def toDict(self):
        return {
            "id": self.id,
            "server": self.server,
            "roomId": self.roomId,
            "locked": self.locked,
        }


class ParamsSalons(SQLObject):
    server = IntCol()
    parametre = StringCol()
    roomId = IntCol()

    def toDict(self):
        return {
            "id": self.id,
            "server": self.server,
            "parametre": self.parametre,
            "roomId": self.roomId,
        }


class ParamsOnOff(SQLObject):
    server = IntCol()
    parametre = StringCol()
    status = IntCol()

    def toDict(self):
        return {
            "id": self.id,
            "server": self.server,
            "parametre": self.parametre,
            "status": self.status,
        }


class Owners(SQLObject):
    server = IntCol()
    userId = IntCol()

    def toDict(self):
        return {
            "id": self.id,
            "server": self.server,
            "userId": self.userId,
        }

class Blacklist(SQLObject):
    server = IntCol()
    userId = IntCol()
    username = StringCol()
    
    def toDict(self):
        return {
            "id": self.id,
            "server": self.server,
            "userId": self.userId,
            "username": self.username,
        }

class Whitelist(SQLObject):
    server = IntCol()
    userId = IntCol()
    username = StringCol()

    def toDict(self):
        return {
            "id": self.id,
            "server": self.server,
            "userId": self.userId,
            "username": self.username,
        }

class VocMutes(SQLObject):
    server = IntCol()
    pseudo = StringCol()
    userId = StringCol()
    reason = StringCol()
    until = DateTimeCol()

    def toDict(self):
        return {
            "id": self.id,
            "server": self.server,
            "pseudo": self.pseudo,
            "userId": self.userId,
            "reason": self.reason,
            "until": self.until,
        }
    
class Custom(SQLObject):
    server = IntCol()
    name = StringCol()
    response = StrincCol()
    embed = StringCol()

    def toDict(self):
        return {
            "id": self.id,
            "server": self.server,
            "name": self.name,
            "response": self.response,
            "embed": self.embed,
        }

class Money(SQLObject):
    server = IntCol()
    money = IntCol()
    type = StringCol()

    def toDict(self):
        return {
            "id": self.id,
            "server": self.server,
            "money": self.money,
            "type": self.type,
        }

class TicketsEmbed(SQLObject):
    server = IntCol()
    roomId = IntCol()
    embedId = IntCol()
    title = StringCol()
    buttonText = StringCol()
    buttonColor = IntCol()

    def toDict(self):
        return {
            "id": self.id,
            "server": self.server,
            "rooId": self.money,
            "embedId": self.money,
            "title": self.title,
            "buttonText": self.buttonText,
            "buttonColor": self.buttonColor,
        }


class Tickets(SQLObject):
    server = IntCol()
    
    


# class Pronote(SQLObject):
#     pass


Users.createTable(ifNotExists=True)
Warns.createTable(ifNotExists=True)
Kicks.createTable(ifNotExists=True)
Bans.createTable(ifNotExists=True)
Mutes.createTable(ifNotExists=True)
RoomsLocker.createTable(ifNotExists=True)
ParamsSalons.createTable(ifNotExists=True)
ParamsOnOff.createTable(ifNotExists=True)
Owners.createTable(ifNotExists=True)