class Runner:
    """
    A runner

    >>>print(r1)
    Email: dave.sanchez@utoronto.mail.ca
    Time to finish: 45 minutes
    Average speed: 6.66 km/h

    Attributes:
    ===========
    @type email: str
        email address of runner
    @type time: float
        estimated time it takes for runner to finish the 5k marathon in minutes
    @type speed: float
        calculated average speed of runner in km/h
    """

    def __init__(self, email, time):
        """
        Initialize a runner with a given email address and time to finish
        the race.

        @type self: Runner
        @type email: str
            email address of runner
        @type time: float
            estimated time to finish race
        @type speed: float
            calculated time to finish race
        @rType: None
        """
        self.email, self.time, self.speed = str(email), float(time), float(5/(time/60))

    def __str__(self):
        """
        Return a string of a runner's email and their time to finish.

        @type self: Runner
        @rtype: str

        >>> r = Runner(dave.sanchez@mail.utoronto.ca, 45)
        >>> print(r)
        Email: dave.sanchez@utoronto.mail.ca
        Time to finish: 45 minutes
        Average speed: 6.66 km/h
        """

        return "Email address: {} \nTime to finish: {} \nAverage Speed: {}".format(self.email, self.time, self.s)

    def __eq__(self, other):
        """
        Compare runners' speeds.

        @type self: Runner
        @rtype: bool

        >>> r1 = Runner(runner.1@mail.utoronto.ca, 50)
        >>> r2 = Runner(runner.2@mail.utoronto.ca, 45)
        >>> r1 = r2
        False
        """

        return self.speed == other.speed

    def __lt__(self, other):
        """
        Compare runners' speeds.

        @type self: Runner
        @rtype: bool

        >>> r1 = Runner(runner.1@mail.utoronto.ca, 50)
        >>> r2 = Runner(runner.2@mail.utoronto.ca, 45)
        >>> r1 < r2
        True
        """

        return self.speed < other.speed

    def __gt__(self, other):
        """
        Compare runners' speeds.

        @type self: Runner
        @rtype: bool

        >>> r1 = Runner(runner.1@mail.utoronto.ca, 50)
        >>> r2 = Runner(runner.2@mail.utoronto.ca, 45)
        >>> r1 > r2
        False
        """

        return self.speed > other.speed

