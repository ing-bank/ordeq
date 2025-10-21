from ordeq import RunHook


class _MyHook(RunHook):
    def before_run(self, *args, **kwargs):
        print("Starting the run")

    def after_run(self, *args, **kwargs):
        print("Finished the run")


MyHook = _MyHook()

other_obj = 123
