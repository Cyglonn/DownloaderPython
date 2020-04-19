print("test")

import libpyanidb.anidb as anidb

db = anidb.AniDBInterface()

db.auth("yaclo52", "Moustaki47")

print(db.user("yaclo52"))
print(db.randomanime(0))