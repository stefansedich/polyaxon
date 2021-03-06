from constants.statuses import BaseStatuses, StatusOptions


class ExperimentGroupLifeCycle(BaseStatuses):
    """Experiment group lifecycle

    Props:
        * CREATED: created and waiting to be scheduled
        * RUNNING: one or all jobs is still running
        * DONE: experiment group has finished scheduling and tracking all experiments
        * FAILED: one of the jobs has failed
        * STOPPED: was stopped/deleted/killed
    """
    CREATED = StatusOptions.CREATED
    RUNNING = StatusOptions.RUNNING
    DONE = StatusOptions.DONE
    FAILED = StatusOptions.FAILED
    STOPPED = StatusOptions.STOPPED

    CHOICES = (
        (CREATED, CREATED),
        (RUNNING, RUNNING),
        (DONE, DONE),
        (FAILED, FAILED),
        (STOPPED, STOPPED),
    )

    VALUES = {
        CREATED, RUNNING, DONE, FAILED, STOPPED
    }

    PENDING_STATUS = {CREATED, }
    RUNNING_STATUS = {RUNNING, }
    DONE_STATUS = {FAILED, STOPPED, DONE}
    FAILED_STATUS = {FAILED, }

    TRANSITION_MATRIX = {
        CREATED: {None, },
        RUNNING: {CREATED, STOPPED},
        DONE: {RUNNING, },
        FAILED: {CREATED, RUNNING},
        STOPPED: set(VALUES) - {STOPPED, },
    }
