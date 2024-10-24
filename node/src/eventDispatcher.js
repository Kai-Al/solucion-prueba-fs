var EventDispatcher = {
  /**
   * @param {object} instance
   * @return {void}
   */
  mixin: function (instance) {},

  /**
   * @param {string} name
   * @param {function} callback
   * @param {Object} opt_scope
   * @return {void}
   */
  addEventListener: function (name, callback, opt_scope) {},

  /**
   * @param {string} name
   * @return {boolean}
   */
  hasListenerFor: function (name) {},

  /**
   * @param {string} name
   * @param {function} callback
   * @return {boolean}
   */
  hasCallbackFor: function (name, callback) {},

  /**
   * @param {string} name
   * @param {function} callback
   * @param {Object} opt_scope
   * @return {void}
   */
  removeEventListener: function (name, callback, opt_scope) {},

  /**
   * @param {string} name
   * @return {void}
   */
  dispatchEvent: function (name) {},
};
