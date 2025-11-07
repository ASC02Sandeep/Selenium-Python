class InvalidOperationError(Exception):
    """Custom exception for invalid operations."""
    def __init__(self, message="Invalid operation encountered"):
        super().__init__(message)
        self.message = message