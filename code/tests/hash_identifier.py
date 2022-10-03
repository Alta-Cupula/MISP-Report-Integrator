from hashid import HashID

_hash = "3ce8b0ffd75bc240fc7d967729cd6637"

identifier = HashID()

results = identifier.identifyHash(_hash)

print([type.name for type in results])
