class Voiture:

    def __init__(self, model):
        self._model = model
        self._nb_roue = 4

    # Props Model
    def _get_model(self):
        return self._model.upper()

    def _set_model(self, value):
        self._model = value

    model = property(_get_model, _set_model)


    # Props _nb_roue
    def _get_nb_roue(self):
        return self._nb_roue

    def _set_nb_roue(self, value):
        if value >= 2 :
            self._nb_roue = value
        else:
            self._nb_roue = 2

    nb_roue = property(_get_nb_roue, _set_nb_roue)
