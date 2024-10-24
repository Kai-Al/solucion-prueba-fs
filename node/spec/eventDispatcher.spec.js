describe('EventDispatcher System', () => {
  describe('Mixin method', () => {
    it('Should mix in EventDispatcher methods on given object', () => {
      let testObj = {}
      EventDispatcher.mixin(testObj)

      expect(typeof testObj.addEventListener).toBe('function')
      expect(typeof testObj.dispatchEvent).toBe('function')
      expect(typeof testObj.removeEventListener).toBe('function')
      expect(typeof testObj.hasListenerFor).toBe('function')
      expect(typeof testObj.hasCallbackFor).toBe('function')
    })
  })

  describe('Adding event listeners', () => {
    let testObj
    const testFunction = function () {
      console.log('a test function')
    }
    const testFunction2 = function () {
      console.log('another test function')
    }
    const testEventName = 'testEvent'

    beforeEach(() => {
      testObj = {}
      EventDispatcher.mixin(testObj)
    })

    it('Should save listener event for given name', () => {
      testObj.addEventListener(testEventName, testFunction)

      expect(testObj.hasListenerFor(testEventName)).toBe(true)
    })

    it('Should save event with callback and event name', () => {
      testObj.addEventListener(testEventName, testFunction)

      expect(testObj.hasCallbackFor(testEventName, testFunction)).toBe(true)
    })

    it('Should save multiple callbacks for given event name', () => {
      testObj.addEventListener(testEventName, testFunction)
      testObj.addEventListener(testEventName, testFunction2)

      expect(testObj.hasListenerFor(testEventName)).toBe(true)
      expect(testObj.hasCallbackFor(testEventName, testFunction)).toBe(true)
      expect(testObj.hasCallbackFor(testEventName, testFunction2)).toBe(true)
    })

    it('Should not share store between different instances', () => {
      let testObj2 = {}
      EventDispatcher.mixin(testObj2)
      testObj.addEventListener(testEventName, testFunction)

      expect(testObj.hasCallbackFor(testEventName, testFunction)).toBe(true)
      expect(testObj2.hasCallbackFor(testEventName, testFunction)).toBe(false)
    })
  })

  describe('Assert presence of listeners', () => {
    let testObj
    const testFunction = function () {
      console.log('a test function')
    }
    const testFunction2 = function () {
      console.log('another test function')
    }
    const testEventName = 'testEvent'

    beforeEach(() => {
      testObj = {}
      EventDispatcher.mixin(testObj)
    })

    it('Should return false hasListenerFor if event name is not added', () => {
      testObj.addEventListener(testEventName, testFunction)

      expect(testObj.hasListenerFor('xxx')).toBe(false)
    })

    it('Should return false hasCallbackFor if method is not added', () => {
      testObj.addEventListener(testEventName, testFunction)

      expect(testObj.hasCallbackFor(testEventName, testFunction)).toBe(true)
      expect(testObj.hasCallbackFor(testEventName, testFunction2)).toBe(false)
    })
  })

  describe('Removing event listeners', () => {
    let testObj
    const testFunction = function () {
      console.log('a test function')
    }
    const testFunction2 = function () {
      console.log('another test function')
    }
    const testEventName = 'testEvent'

    beforeEach(() => {
      testObj = {}
      EventDispatcher.mixin(testObj)
    })

    it('Should remove certain callback from related event name', () => {
      testObj.addEventListener(testEventName, testFunction)
      testObj.addEventListener(testEventName, testFunction2)
      testObj.removeEventListener(testEventName, testFunction)

      expect(testObj.hasCallbackFor(testEventName, testFunction2)).toBe(true)
      expect(testObj.hasCallbackFor(testEventName, testFunction)).toBe(false)
    })

    it('Should remove event name registered if all related callbacks are removed', () => {
      testObj.addEventListener(testEventName, testFunction)
      testObj.removeEventListener(testEventName, testFunction)

      expect(testObj.hasListenerFor(testEventName)).toBe(false)
    })
  })

  describe('Dispatching events', () => {
    let testObj
    const testFunction = jasmine.createSpy('testFunction')
    const testFunction2 = jasmine.createSpy('testFunction2')
    const testEventName = 'testEvent'

    beforeEach(() => {
      testObj = {}
      EventDispatcher.mixin(testObj)
    })

    afterEach(() => {
      testFunction.calls.reset()
      testFunction2.calls.reset()
    })

    it('Should call registered callbacks when event fired', () => {
      testObj.addEventListener(testEventName, testFunction)
      testObj.addEventListener(testEventName, testFunction2)
      testObj.dispatchEvent(testEventName)

      expect(testFunction).toHaveBeenCalled()
      expect(testFunction2).toHaveBeenCalled()
    })

    it('Should not call registered callback if removed', () => {
      testObj.addEventListener(testEventName, testFunction)
      testObj.addEventListener(testEventName, testFunction2)
      testObj.removeEventListener(testEventName, testFunction2)
      testObj.dispatchEvent(testEventName)

      expect(testFunction).toHaveBeenCalled()
      expect(testFunction2).not.toHaveBeenCalled()
    })

    it('Should allow callbacks to be executed in a given scope', () => {
      const scope = { executeSuccess: true }
      let success = false
      const testScopedFunction = function () {
        if (this.executeSuccess) success = true
      }
      testObj.addEventListener(testEventName, testScopedFunction, scope)
      testObj.dispatchEvent(testEventName)
      expect(success).toBe(true)
    })
  })
})