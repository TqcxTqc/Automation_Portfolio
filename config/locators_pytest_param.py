class ParametrizationData:
    """
    Contains parametrization data for pytest
    """
    CLOTH_OPTIONS_TITLE = ['Category', 'Style', 'Size', 'Price', 'Color', 'Material', 'Eco Collection',
                           'Performance Fabric', 'Erin Recommends', 'New', 'Sale', 'Pattern', 'Climate']


class ClothColor:
    """
    Locators for cloth colors, can be used for MEN / WOMEN cloths
    """
    BLUE_COLOR = "#option-label-color-93-item-50"
    PURPLE_COLOR = "#option-label-color-93-item-57"
    BLACK_COLOR = "#option-label-color-93-item-49"
    YELLOW_COLOR = "#option-label-color-93-item-60"
    WHITE_COLOR = "#option-label-color-93-item-59"
    RED_COLOR = "#option-label-color-93-item-58"
    GREEN_COLOR = "#option-label-color-93-item-53"
    ORANGE_COLOR = "#option-label-color-93-item-56"


class ClothSize:
    """
    Locators for cloth size, can be used for MEN / WOMEN cloths
    """
    XS = "#option-label-size-143-item-166"
    S = "#option-label-size-143-item-167"
    M = "#option-label-size-143-item-168"
    L = "#option-label-size-143-item-169"
    XL = "#option-label-size-143-item-170"


class BaseLocators:
    ALERT_SUCCESS = "div.message-success"
    SHOP_OPTIONS_CATEGORY = "#narrow-by-list .filter-options-title"
