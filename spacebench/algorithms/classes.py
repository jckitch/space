from abc import abstractmethod

from spacebench.env import SpaceDataset


class SpatialMethod:
    @abstractmethod
    def fit(self, dataset: SpaceDataset, **kwargs) -> None:
        """Estimates the causal effect of a treatment on an outcome.
        The available estimands are defined by the estimands() method.
        The method must either return a single dictionary with the
        estimand as key and the estimated effect as value or a tuple
        of two dictionaries, where the first dictionary contains the
        estimands and the second dictionary contains additional information
        about the estimation process.

        Arguments
        _________
        dataset : SpaceDataset
            The dataset used to learn the causal effect.
        """
        pass

    @property
    @abstractmethod
    def available_estimands(self) -> list[str]:
        """Aavailable estimands.

        Returns
        _______
        list[str]
            A list of available estimands (erf, ate, att, ite, etc.)
        """
        pass

    @abstractmethod
    def eval(self, dataset: SpaceDataset) -> dict[str, float | list[float]]:
        """Return a dictionary with the estimated effects for all
        available estimands.

        Arguments
        _________
        dataset : SpaceDataset
            The dataset to be evaluated.

        Returns
        _______
        dict[str, float | list[float]]
            A dictionary with the estimands as keys and the estimated
            effects as values.
        """
        pass
