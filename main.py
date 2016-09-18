import traceback

class Trace(object):
	@staticmethod
	def log(type, msg):
		print "[{type}] {msg}".format(
			type = type,
			msg = msg
			)
		pass
	pass

class Notification(object):
	observers = {}

	@staticmethod
	def addObserver(observer, event):
		if event is None:
			Trace.log("Notification", "event is None")
			return False
			pass

		if observer is None:
			Trace.log("Notification", "observer is None")
			return False
			pass

		if event not in Notification.observers.keys():
			Notification.observers[event] = []
			pass

		Notification.observers[event].append(observer)

		return True
		pass

	@staticmethod
	def notify(event, *args, **kwargs):
		if event not in Notification.observers.keys():
			Trace.log(
				"Notification", 
				"event {event} not in observers {observers}".format(
					event = event,
					observers = Notification.observers
					)
				)
			return False
			pass

		for observer in Notification.observers[event]:
			observer.update(event, *args, **kwargs)
			pass

		return True
		pass
	pass

class ModelChatBot(object):
	def __init__(self):
		self.is_running = False
		self.db = {}

		Notification.addObserver(self, "onStop")
		pass

	def isRunning(self):
		return is_running
		pass

	def run(self):
		is_running = True

		Notification.notify("onStart")
		# Notification.notify("onStop")
		pass

	def update(self, event, *args, **kwargs):
		if event == "onStop":
			self.stop()
			pass
		pass

	def stop(self):
		self.is_running = False
		pass
	pass

class ViewChatBot(object):
	def __init__(self, model):
		self.model = model

		Notification.addObserver(self, "onAskQuestion")
		Notification.addObserver(self, "onPrint")
		pass

	def update(self, event, *args, **kwargs):
		if event == "onAskQuestion":
			self.ask(kwargs["question"])
			pass
		if event == "onPrint":
			self.ask(kwargs["msg"])
			pass
		pass

	def ask(self, question):
		print question
		pass

	def print_msg(self, msg):
		print msg
		pass
	pass

class ControllerChatBot(object):
	def __init__(self, model):
		self.model = model

		Notification.addObserver(self, "onStart")
		pass

	def update(self, event, *args, **kwargs):
		if event == "onStart":
			self.ask_name()
			pass
		pass

	def ask_name(self):
		question = "What is your name?"
		Notification.notify("onAskQuestion", question=question)

		answer = self.get_input()

		msg = "Hi {name}!".format(name=answer)
		Notification.notify("onPrint", msg=msg)
		pass

	def get_input(self):
		user_input = raw_input(">")

		return user_input
		pass
	pass

def main():
	model = ModelChatBot()
	controller = ControllerChatBot(model)
	view = ViewChatBot(model)

	model.run()

	pass

if __name__ == "__main__":
	main()
	pass
