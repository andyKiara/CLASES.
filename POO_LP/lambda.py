lista_alumnos=[
  {
     "nombre":"edwin",
     "edad":15,
     "hobby":"danza",
     "flaquita":"melody"
  },
  {
     "nombre":"del mar",
     "edad":30,
     "hobby":"saltar",
     "flaquita":"melody"
  },
  {
     "nombre":"orlando",
     "edad":14,
     "hobby":"ponchar",
     "flaquita":"samy"
  },
  {
     "nombre":"jory",
     "edad":50,
     "hobby":"aplicar",
     "flaquita":"samy"
  },
  {
     "nombre":"hans",
     "edad":13,
     "hobby":"quemarse",
     "flaquita":"hermana"
  }
]
print(f"todos mis alumnitos {lista_alumnos}")
fans_melody=list(filter(lambda par:par
["flaquita"]=="melody",lista_alumnos))
print(f"los que quieren con melody {fans_melody}")