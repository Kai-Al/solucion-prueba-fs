const EventDispatcher = {
  /**
   * Mezcla los métodos del EventDispatcher en una instancia dada.
   * @param {object} instance - El objeto al que se le añadirán los métodos del EventDispatcher.
   * @return {void}
   */
  mixin: function (instance) {
    // Inicializa el almacén de eventos para la instancia
    instance._eventStore = {};

    // Asigna los métodos del EventDispatcher a la instancia
    instance.addEventListener = this.addEventListener;
    instance.removeEventListener = this.removeEventListener;
    instance.dispatchEvent = this.dispatchEvent;
    instance.hasListenerFor = this.hasListenerFor;
    instance.hasCallbackFor = this.hasCallbackFor;
  },

  /**
   * Agrega un listener (callback) para un nombre de evento específico.
   * @param {string} name - El nombre del evento.
   * @param {function} callback - La función a llamar cuando se dispare el evento.
   * @param {Object} opt_scope - (Opcional) El scope en el cual se ejecutará el callback.
   * @return {void}
   */
  addEventListener: function (name, callback, opt_scope) {
    // Si no existe una lista de listeners para este evento, crea una nueva
    if (!this._eventStore[name]) {
      this._eventStore[name] = [];
    }
    // Añade el listener a la lista del evento
    this._eventStore[name].push({
      callback: callback,
      scope: opt_scope || null, // Usa el scope proporcionado o null si no se proporciona
    });
  },

  /**
   * Remueve un listener específico para un nombre de evento dado.
   * @param {string} name - El nombre del evento.
   * @param {function} callback - La función callback a remover.
   * @param {Object} opt_scope - (Opcional) El scope asociado al callback.
   * @return {void}
   */
  removeEventListener: function (name, callback, opt_scope) {
    // Si no hay listeners para este evento, no hay nada que hacer
    if (!this._eventStore[name]) {
      return;
    }
    // Filtra los listeners que no coinciden con el callback y scope proporcionados
    this._eventStore[name] = this._eventStore[name].filter((listener) => {
      return (
        listener.callback !== callback || listener.scope !== (opt_scope || null)
      );
    });
    // Si no quedan listeners para este evento, elimina la entrada del almacén
    if (this._eventStore[name].length === 0) {
      delete this._eventStore[name];
    }
  },

  /**
   * Verifica si hay listeners registrados para un nombre de evento dado.
   * @param {string} name - El nombre del evento.
   * @return {boolean} - True si hay listeners, false en caso contrario.
   */
  hasListenerFor: function (name) {
    // Retorna true si existe una lista de listeners y no está vacía
    return !!(this._eventStore[name] && this._eventStore[name].length > 0);
  },

  /**
   * Verifica si un callback específico está registrado para un evento.
   * @param {string} name - El nombre del evento.
   * @param {function} callback - El callback a verificar.
   * @return {boolean} - True si el callback está registrado, false en caso contrario.
   */
  hasCallbackFor: function (name, callback) {
    // Si no hay listeners para este evento, retorna false
    if (!this._eventStore[name]) {
      return false;
    }
    // Verifica si el callback está en la lista de listeners
    return this._eventStore[name].some((listener) => {
      return listener.callback === callback;
    });
  },

  /**
   * Despacha un evento, llamando a todos los callbacks registrados para ese nombre.
   * @param {string} name - El nombre del evento a despachar.
   * @return {void}
   */
  dispatchEvent: function (name) {
    // Si no hay listeners para este evento, no hay nada que hacer
    if (!this._eventStore[name]) {
      return;
    }
    // Crea una copia de la lista de listeners para evitar problemas si se modifican durante la iteración
    const listeners = this._eventStore[name].slice();
    // Itera sobre cada listener y ejecuta su callback con el scope adecuado
    for (const listener of listeners) {
      listener.callback.call(listener.scope || this);
    }
  },
};
