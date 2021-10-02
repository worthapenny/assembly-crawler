from typing import TypeVar, overload, Generic

TNetworkUnitsType = TypeVar("TNetworkUnitsType", INetworkUnits)
TComponentUnitsType = TypeVar("TComponentUnitsType", IComponentUnits)

class IModelUnits(Generic[TNetworkUnitsType, TComponentUnitsType]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def Units(self) -> IUnits:
		"""
		Returns:
			IUnits`2: No Description
		"""
		pass

class INetworkUnits:

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IComponentUnits:

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IUnits(Generic[TNetworkUnitsType, TComponentUnitsType]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def IUnits(self, value: float, unit: IUnit) -> str:
		"""Method Description

		Args:
			value(float): value
			unit(IUnit): unit

		Returns:
			str: 
		"""
		pass

	@overload
	def IUnits(self, value: float, unit: IUnit, format: int, signficantDigits: int) -> str:
		"""Method Description

		Args:
			value(float): value
			unit(IUnit): unit
			format(int): format
			signficantDigits(int): signficantDigits

		Returns:
			str: 
		"""
		pass

	def ConvertValue(self, value: float, fromUnit: Unit, toUnit: Unit) -> float:
		"""Method Description

		Args:
			value(float): value
			fromUnit(Unit): fromUnit
			toUnit(Unit): toUnit

		Returns:
			float: 
		"""
		pass

	def Reset(self, unitSystem: int) -> None:
		"""Method Description

		Args:
			unitSystem(int): unitSystem

		Returns:
			None: 
		"""
		pass

	@property
	def NetworkUnits(self) -> TNetworkUnitsType:
		"""
		Returns:
			TNetworkUnitsType: No Description
		"""
		pass

	@property
	def ComponentUnits(self) -> TComponentUnitsType:
		"""
		Returns:
			TComponentUnitsType: No Description
		"""
		pass

class IUnit:

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def IUnit(self, value: float) -> str:
		"""Method Description

		Args:
			value(float): value

		Returns:
			str: 
		"""
		pass

	@overload
	def IUnit(self, value: float, format: int, significantDigits: int) -> str:
		"""Method Description

		Args:
			value(float): value
			format(int): format
			significantDigits(int): significantDigits

		Returns:
			str: 
		"""
		pass

	def SetUnit(self, unit: Unit) -> None:
		"""Method Description

		Args:
			unit(Unit): unit

		Returns:
			None: 
		"""
		pass

	def GetUnit(self) -> Unit:
		"""Method Description

		Returns:
			Unit: 
		"""
		pass

	def ConvertTo(self, value: float, unit: Unit) -> float:
		"""Method Description

		Args:
			value(float): value
			unit(Unit): unit

		Returns:
			float: 
		"""
		pass

	@property
	def Dimension(self) -> Dimension:
		"""
		Returns:
			Dimension: No Description
		"""
		pass

	@property
	def FormatCode(self) -> int:
		"""
		Returns:
			int: No Description
		"""
		pass

	@property
	def SignificantDigits(self) -> int:
		"""
		Returns:
			int: No Description
		"""
		pass

	@property
	def Label(self) -> str:
		"""
		Returns:
			str: No Description
		"""
		pass

	@property
	def ShortLabel(self) -> str:
		"""
		Returns:
			str: No Description
		"""
		pass

	@FormatCode.setter
	def FormatCode(self, formatcode: int) -> None:
		pass

	@SignificantDigits.setter
	def SignificantDigits(self, significantdigits: int) -> None:
		pass

