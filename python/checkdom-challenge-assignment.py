class checkdom_challenge_soln:
    def check_dom(str_param: str) -> bool or str:
        """
        Check if an HMTL tag is valid or not.

        Args:
            str_param(str): An input HTML string containing tags.
        
        Return:
            bool or str: Return False if HTML tags are mismatched or invalid
                        Returns mismatched tag if there's only one.
                        Returns True if all tags are matched and valid.
        Examples:
            >>> check_dom("<p>Hello World!</p>")
            True
            
            >>> check_dom("<p>Hello World!</i>")
            'p'

            >>> check_dom("<p>Hello World!")
            False

        HTML Tags to be used:
            The elements that will be used are: <b>, <i>, <em>, <div>, <p>
        """
        tags = ('<b>', '<div>', '<p>')

        # check for existing html tags
        # and find its corr. tag if exists.
        for tag in tags:
            if tag in str_param and f'</{tag}>' in str_param:
                return True
            return False
