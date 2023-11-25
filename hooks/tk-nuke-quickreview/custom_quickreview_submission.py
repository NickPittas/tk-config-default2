import nuke
import sgtk

HookClass = sgtk.get_hook_baseclass()

class CustomQuickReviewSubmission(HookClass):

    def execute(self, **kwargs):
        """
        Main hook entry point
        :returns: None
        """

        # Determine the current colorspace
        if self._is_aces_colorspace():
            quicktime_settings = {
                "colorspace": "Output - sRGB"
                # other settings as needed
            }
        else:
            # Use default settings
            quicktime_settings = {
                # default settings
            }

        # Apply the settings to the QuickReview process
        self.parent.engine.create_quicktime(quicktime_settings)

    def _is_aces_colorspace(self):
        """
        Determines if Nuke is currently using ACES colorspace
        :return: True if in ACES colorspace, False otherwise
        """
        # Example check, you might need to adjust this based on how your Nuke setup identifies ACES
        return "aces_1.2" in nuke.root().knob("OCIO_config").value()
