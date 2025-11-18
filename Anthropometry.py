"""
Ernest Lee Mitchell
Wright State University
November 2, MMXXV
"""

"""
This code features dictionaries that computes the mass, length, and segment center of gravity length
for body segments based on [1]. Includes the following classes.

1.) Anthropometric_Data_Male: Dictionary of body proportions in males.

2.) Anthropometric_Data_Female: Dictionary of body proportions in females.
"""

"""
References:
[1] “ExRx.net: Body segment data,” Body Segment Data, https://exrx.net/Kinesiology/Segments (accessed Oct. 31, 2025). 
""" 

class Anthropometric_Data_Male:
    """
    A class that computes anthropometric data for a male subject.

    Implementation in main method:
    Create an instance computation for Anthropometric_Data_Male.
        body_proportion = Anthropometric_Data_Male()
        <segment_calculation> = body_proportion.<body_segment>(<anatomical_measure>)
    """
    # Conversion factors for body proportions in males.
    # Stored as: Dictionary featuring the following conversion factors: {segment_name: factor_proportion}.
    _proportion_male = {
        'mass_cephalic_male': 0.0826,
        'mass_torso_male': 0.551,
        'mass_thoracic_male': 0.201,
        'mass_abdominal_male': 0.1306,
        'mass_pelvic_male': 0.1366,
        'mass_brachial_male': 0.0325,
        'mass_antebrachial_male': 0.0187,
        'mass_manual_male': 0.0065,
        'mass_femoral_male': 0.105,
        'mass_crural_male': 0.0475,
        'mass_pedal_male': 0.0143,
        'lengthseg_cephalic_male': 0.1075,
        'lengthseg_torso_male': 0.3,
        'lengthseg_thoracic_male': 0.127,
        'lengthseg_abdominal_male': 0.081,
        'lengthseg_pelvic_male': 0.093,
        'lengthseg_brachial_male': 0.172,
        'lengthseg_antebrachial_male': 0.157,
        'lengthseg_manual_male': 0.0575,
        'lengthseg_femoral_male': 0.232,
        'lengthseg_crural_male': 0.247,
        'lengthseg_pedal_male': 0.0425,
        'lengthcg_cephalic_male': 0.55,
        'lengthcg_torso_male': 0.63,
        'lengthcg_thoracic_male': 0.567,
        'lengthcgt_abdominal_male': 0.46,
        'lengthcg_pelvic_male': 0.05,
        'lengthcg_brachial_male': 0.436,
        'lengthcg_antebrachial_male': 0.43,
        'lengthcg_manual_male': 0.468,
        'lengthcg_femoral_male': 0.433,
        'lengthcg_crural_male': 0.434,
        'lengthcg_pedal_male': 0.5,
    }

    # Helper method for conversions.
    def _segmentmale(self, value, factor_key):
        """Internal helper method for simple conversions."""
        factor_male = self._proportion_male.get(factor_key)
        if factor_male is None:
            raise ValueError(f"Conversion factor for '{factor_key}' not found.")
        return value * factor_male

    # I: Mass proporotions of body segments in males. Mass is in kilogram.
    # Cephalic (head).
    def mass_cephalic_male(self, mass):
        """Computes mass of head."""
        return self._segmentmale(mass, 'mass_cephalic_male')
    
    # Torso (chest and abdomen).
    def mass_torso_male(self, mass):
        """Computes mass of torso."""
        return self._segmentmale(mass, 'mass_torso_male')
    
    # Thoracic (chest).
    def mass_thoracic_male(self, mass):
        """Computes mass of chest."""
        return self._segmentmale(mass, 'mass_thoracic_male')
    
    # Abdominal (abdomen).
    def mass_abdominal_male(self, mass):
        """Computes mass of abdomen."""
        return self._segmentmale(mass, 'mass_abdominal_male')
    
    # Pelvic (pelvis).
    def mass_pelvic_male(self, mass):
        """Computes mass of pelvis."""
        return self._segmentmale(mass, 'mass_pelvic_male')
    
    # Brachial (upper arm).
    def mass_brachial_male(self, mass):
        """Computes mass of upper arm."""
        return self._segmentmale(mass, 'mass_brachial_male')
    
    # Antebrachial (forearm).
    def mass_antebrachial_male(self, mass):
        """Computes mass of forearm."""
        return self._segmentmale(mass, 'mass_antebrachial_male')
    
    # Manual (hand).
    def mass_manual_male(self, mass):
        """Computes mass of hand."""
        return self._segmentmale(mass, 'mass_manual_male')
    
    # Femoral (thigh).
    def mass_femoral_male(self, mass):
        """Computes mass of thigh."""
        return self._segmentmale(mass, 'mass_femoral_male')
    
    # Crural (shin).
    def mass_cruralc_male(self, mass):
        """Computes mass of shin."""
        return self._segmentmale(mass, 'mass_crural_male')
    
    # Pedal (foot).
    def mass_pedal_male(self, mass):
        """Computes mass of foot."""
        return self._segmentmale(mass, 'mass_pedal_male')
    
    # II: Height proportions of body segments in males. Lengths is in meters.
    # Cephalic (head).
    def lengthseg_cephalic_male(self, lengthseg):
        """Computes segment length of head."""
        return self._segmentmale(lengthseg, 'lengthseg_cephalic_male')
    
    # Torso (chest and abdomen).
    def lengthseg_torso_male(self, lengthseg):
        """Computes segment length of torso."""
        return self._segmentmale(lengthseg, 'lengthseg_torso_male')
    
    # Thoracic (chest).
    def lengthseg_thoracic_male(self, lengthseg):
        """Computes segment length of chest."""
        return self._segmentmale(lengthseg, 'lengthseg_thoracic_male')
    
    # Abdominal (abdomen).
    def lengthseg_abdominal_male(self, lengthseg):
        """Computes segment length of abdomen."""
        return self._segmentmale(lengthseg, 'lengthseg_abdominal_male')
    
    # Pelvic (pelvis).
    def lengthseg_pelvic_male(self, lengthseg):
        """Computes segment length of pelvis."""
        return self._segmentmale(lengthseg, 'lengthseg_pelvic_male')
    
    # Brachial (upper arm).
    def lengthseg_brachial_male(self, lengthseg):
        """Computes segment length of upper arm."""
        return self._segmentmale(lengthseg, 'lengthseg_brachial_male')
    
    # Antebrachial (forearm).
    def lengthseg_antebrachial_male(self, lengthseg):
        """Computes segment length of forearm."""
        return self._segmentmale(lengthseg, 'lengthseg_antebrachial_male')
    
    # Manual (hand).
    def lengthseg_manual_male(self, lengthseg):
        """Computes segment length of hand."""
        return self._segmentmale(lengthseg, 'lengthseg_manual_male')
    
    # Femoral (thigh).
    def lengthseg_femoral_male(self, lengthseg):
        """Computes segment length of thigh."""
        return self._segmentmale(lengthseg, 'lengthseg_femoral_male')
    
    # Crural (shin).
    def lengthseg_cruralc_male(self, lengthseg):
        """Computes segment length of shin."""
        return self._segmentmale(lengthseg, 'lengthseg_crural_male')
    
    # Pedal (foot).
    def lengthseg_pedal_male(self, lengthseg):
        """Computes segment length of foot."""
        return self._segmentmale(lengthseg, 'lengthseg_pedal_male')
    
    # III: Segmental center of gravity locations in males. Measured in meters.
    # Cephalic (head).
    def lengthcg_cephalic_male(self, lengthcg):
        """Computes segment center of gravity of head."""
        return self._segmentmale(lengthcg, 'lengthcg_cephalic_male')
    
    # Torso (chest and abdomen).
    def lengthcg_torso_male(self, lengthcg):
        """Computes segment center of gravity length of torso."""
        return self._segmentmale(lengthcg, 'lengthcg_torso_male')
    
    # Thoracic (chest).
    def lengthcg_thoracic_male(self, lengthcg):
        """Computes segment center of gravity length of chest."""
        return self._segmentmale(lengthcg, 'lengthcg_thoracic_male')
    
    # Abdominal (abdomen).
    def lengthcg_abdominal_male(self, lengthcg):
        """Computes segment center of gravity length of abdomen."""
        return self._segmentmale(lengthcg, 'lengthcg_abdominal_male')
    
    # Pelvic (pelvis).
    def lengthcg_pelvic_male(self, lengthcg):
        """Computes segment center of gravity length of pelvis."""
        return self._segmentmale(lengthcg, 'lengthcg_pelvic_male')
    
    # Brachial (upper arm).
    def lengthcg_brachial_male(self, lengthcg):
        """Computes segment center of gravity length of upper arm."""
        return self._segmentmale(lengthcg, 'lengthcg_brachial_male')
    
    # Antebrachial (forearm).
    def lengthcg_antebrachial_male(self, lengthcg):
        """Computes segment center of gravity length of forearm."""
        return self._segmentmale(lengthcg, 'lengthcg_antebrachial_male')
    
    # Manual (hand).
    def lengthcg_manual_male(self, lengthcg):
        """Computes segment center of gravity length of hand."""
        return self._segmentmale(lengthcg, 'lengthcg_manual_male')
    
    # Femoral (thigh).
    def lengthcg_femoral_male(self, lengthcg):
        """Computes segment center of gravity length of thigh."""
        return self._segmentmale(lengthcg, 'lengthcg_femoral_male')
    
    # Crural (shin).
    def lengthcg_cruralc_male(self, lengthcg):
        """Computes segment center of gravity length of shin."""
        return self._segmentmale(lengthcg, 'lengthcg_crural_male')
    
    # Pedal (foot).
    def lengthcg_pedal_male(self, lengthcg):
        """Computes segment center of gravity length of foot."""
        return self._segmentmale(lengthcg, 'lengthcg_pedal_male')

class Anthropometric_Data_Female:
    """
    A class that computes anthropometric data for a female subject.

    Implementation in main method:
    Create an instance computation for Anthropometric_Data_Male.
        body_proportion = Anthropometric_Data_Male()
        <segment_calculation> = body_proportion.<body_segment>(<anatomical_measure>)
    """
    # Conversion factors for body proportions in females.
    # Stored as: Dictionary featuring the following conversion factors: {segment_name: factor_proportion}.
    _proportion_female = {
        'mass_cephalic_female': 0.082,
        'mass_torso_female': 0.532,
        'mass_thoracic_female': 0.1702,
        'mass_abdominal_female': 0.1224,
        'mass_pelvic_female': 0.1596,
        'mass_brachial_female': 0.029,
        'mass_antebrachial_female': 0.0157,
        'mass_manual_female': 0.005,
        'mass_femoral_female': 0.1175,
        'mass_crural_female': 0.0535,
        'mass_pedal_female': 0.0133,
        'lengthseg_cephalic_female': 0.1075,
        'lengthseg_torso_female': 0.29,
        'lengthseg_thoracic_female': 0.127,
        'lengthseg_abdominal_female': 0.081,
        'lengthseg_pelvic_female': 0.093,
        'lengthseg_brachial_female': 0.173,
        'lengthseg_antebrachial_female': 0.16,
        'lengthseg_manual_female': 0.0575,
        'lengthseg_femoral_female': 0.249,
        'lengthseg_crural_female': 0.257,
        'lengthseg_pedal_female': 0.0425,
        'lengthcg_cephalic_female': 0.55,
        'lengthcg_torso_female': 0.569,
        'lengthcg_thoracic_female': 0.563,
        'lengthcgt_abdominal_female': 0.46,
        'lengthcg_pelvic_female': 0.05,
        'lengthcg_brachial_female': 0.458,
        'lengthcg_antebrachial_female': 0.434,
        'lengthcg_manual_female': 0.468,
        'lengthcg_femoral_female': 0.428,
        'lengthcg_crural_female': 0.419,
        'lengthcg_pedal_female': 0.5,
    }

    # Helper method for conversions.
    def _segmentfemale(self, value, factor_key):
        """Internal helper method for simple conversions."""
        factor_female = self._proportion_female.get(factor_key)
        if factor_female is None:
            raise ValueError(f"Conversion factor for '{factor_key}' not found.")
        return value * factor_female

    # I: Mass proporotions of body segments in females. Mass is in kilogram.
    # Cephalic (head).
    def mass_cephalic_female(self, mass):
        """Computes mass of head."""
        return self._segmentfemale(mass, 'mass_cephalic_female')
    
    # Torso (chest and abdomen).
    def mass_torso_female(self, mass):
        """Computes mass of torso."""
        return self._segmentfemale(mass, 'mass_torso_female')
    
    # Thoracic (chest).
    def mass_thoracic_female(self, mass):
        """Computes mass of chest."""
        return self._segmentfemale(mass, 'mass_thoracic_female')
    
    # Abdominal (abdomen).
    def mass_abdominal_female(self, mass):
        """Computes mass of abdomen."""
        return self._segmentfemale(mass, 'mass_abdominal_female')
    
    # Pelvic (pelvis).
    def mass_pelvic_female(self, mass):
        """Computes mass of pelvis."""
        return self._segmentfemale(mass, 'mass_pelvic_female')
    
    # Brachial (upper arm).
    def mass_brachial_female(self, mass):
        """Computes mass of upper arm."""
        return self._segmentfemale(mass, 'mass_brachial_female')
    
    # Antebrachial (forearm).
    def mass_antebrachial_female(self, mass):
        """Computes mass of forearm."""
        return self._segmentfemale(mass, 'mass_antebrachial_female')
    
    # Manual (hand).
    def mass_manual_female(self, mass):
        """Computes mass of hand."""
        return self._segmentfemale(mass, 'mass_manual_female')
    
    # Femoral (thigh).
    def mass_femoral_female(self, mass):
        """Computes mass of thigh."""
        return self._segmentfemale(mass, 'mass_femoral_female')
    
    # Crural (shin).
    def mass_cruralc_female(self, mass):
        """Computes mass of shin."""
        return self._segmentfemale(mass, 'mass_crural_female')
    
    # Pedal (foot).
    def mass_pedal_female(self, mass):
        """Computes mass of foot."""
        return self._segmentfemale(mass, 'mass_pedal_female')
    
    # II: Height proportions of body segments in females. Lengths is in meters.
    # Cephalic (head).
    def lengthseg_cephalic_female(self, lengthseg):
        """Computes segment length of head."""
        return self._segmentfemale(lengthseg, 'lengthseg_cephalic_female')
    
    # Torso (chest and abdomen).
    def lengthseg_torso_female(self, lengthseg):
        """Computes segment length of torso."""
        return self._segmentfemale(lengthseg, 'lengthseg_torso_female')
    
    # Thoracic (chest).
    def lengthseg_thoracic_female(self, lengthseg):
        """Computes segment length of chest."""
        return self._segmentfemale(lengthseg, 'lengthseg_thoracic_female')
    
    # Abdominal (abdomen).
    def lengthseg_abdominal_female(self, lengthseg):
        """Computes segment length of abdomen."""
        return self._segmentfemale(lengthseg, 'lengthseg_abdominal_female')
    
    # Pelvic (pelvis).
    def lengthseg_pelvic_female(self, lengthseg):
        """Computes segment length of pelvis."""
        return self._segmentfemale(lengthseg, 'lengthseg_pelvic_female')
    
    # Brachial (upper arm).
    def lengthseg_brachial_female(self, lengthseg):
        """Computes segment length of upper arm."""
        return self._segmentfemale(lengthseg, 'lengthseg_brachial_female')
    
    # Antebrachial (forearm).
    def lengthseg_antebrachial_female(self, lengthseg):
        """Computes segment length of forearm."""
        return self._segmentfemale(lengthseg, 'lengthseg_antebrachial_female')
    
    # Manual (hand).
    def lengthseg_manual_female(self, lengthseg):
        """Computes segment length of hand."""
        return self._segmentfemale(lengthseg, 'lengthseg_manual_female')
    
    # Femoral (thigh).
    def lengthseg_femoral_female(self, lengthseg):
        """Computes segment length of thigh."""
        return self._segmentfemale(lengthseg, 'lengthseg_femoral_female')
    
    # Crural (shin).
    def lengthseg_cruralc_female(self, lengthseg):
        """Computes segment length of shin."""
        return self._segmentfemale(lengthseg, 'lengthseg_crural_female')
    
    # Pedal (foot).
    def lengthseg_pedal_female(self, lengthseg):
        """Computes segment length of foot."""
        return self._segmentfemale(lengthseg, 'lengthseg_pedal_female')
    
    # III: Segmental center of gravity locations in males. Measured in meters.
    # Cephalic (head).
    def lengthcg_cephalic_female(self, lengthcg):
        """Computes segment center of gravity of head."""
        return self._segmentfemale(lengthcg, 'lengthcg_cephalic_female')
    
    # Torso (chest and abdomen).
    def lengthcg_torso_female(self, lengthcg):
        """Computes segment center of gravity length of torso."""
        return self._segmentfemale(lengthcg, 'lengthcg_torso_female')
    
    # Thoracic (chest).
    def lengthcg_thoracic_female(self, lengthcg):
        """Computes segment center of gravity length of chest."""
        return self._segmentfemale(lengthcg, 'lengthcg_thoracic_female')
    
    # Abdominal (abdomen).
    def lengthcg_abdominal_female(self, lengthcg):
        """Computes segment center of gravity length of abdomen."""
        return self._segmentfemale(lengthcg, 'lengthcg_abdominal_female')
    
    # Pelvic (pelvis).
    def lengthcg_pelvic_female(self, lengthcg):
        """Computes segment center of gravity length of pelvis."""
        return self._segmentfemale(lengthcg, 'lengthcg_pelvic_female')
    
    # Brachial (upper arm).
    def lengthcg_brachial_female(self, lengthcg):
        """Computes segment center of gravity length of upper arm."""
        return self._segmentfemale(lengthcg, 'lengthcg_brachial_female')
    
    # Antebrachial (forearm).
    def lengthcg_antebrachial_female(self, lengthcg):
        """Computes segment center of gravity length of forearm."""
        return self._segmentfemale(lengthcg, 'lengthcg_antebrachial_female')
    
    # Manual (hand).
    def lengthcg_manual_female(self, lengthcg):
        """Computes segment center of gravity length of hand."""
        return self._segmentfemale(lengthcg, 'lengthcg_manual_female')
    
    # Femoral (thigh).
    def lengthcg_femoral_female(self, lengthcg):
        """Computes segment center of gravity length of thigh."""
        return self._segmentfemale(lengthcg, 'lengthcg_femoral_female')
    
    # Crural (shin).
    def lengthcg_cruralc_female(self, lengthcg):
        """Computes segment center of gravity length of shin."""
        return self._segmentfemale(lengthcg, 'lengthcg_crural_female')
    
    # Pedal (foot).
    def lengthcg_pedal_female(self, lengthcg):
        """Computes segment center of gravity length of foot."""
        return self._segmentfemale(lengthcg, 'lengthcg_pedal_female')
    