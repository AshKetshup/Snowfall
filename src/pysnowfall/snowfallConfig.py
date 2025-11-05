class SnowfallConfig():
    """Snowfall Configuration class"""

    TIMESTAMP_BITS        : int = 41
    MACHINE_ID_BITS       : int = 10
    MACHINE_SEQUENCE_BITS : int = 12
    
    def __init__(self, epoch: int = 1_275_350_400_000, workedID: int = 1) -> None: 
        """
        Constructs an instance of SnowfallConfig.

        Args:
            epoch (int, optional): The epoch timestamp in milliseconds. Defaults to 1_275_350_400_000.
            workedID (int, optional): The worker ID. Defaults to 1.
        """        
        self._workedID : int = workedID
        self._epoch    : int = epoch


    @property
    def WorkedID(self) -> int: 
        """The worker ID"""
        return self._workedID

    @WorkedID.setter
    def WorkedID(self, workedID: int) -> None: 
        self._workedID = workedID

    @property
    def Epoch(self) -> int:
        """The epoch timestamp in milliseconds"""        
        return self._epoch
    
    @Epoch.setter
    def Epoch(self, epoch: int) -> None:
        self._epoch = epoch

    