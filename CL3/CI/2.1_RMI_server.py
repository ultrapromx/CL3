import Pyro4

@Pyro4.expose
class StringConcatenator(object):
    def concatenate(self, str1, str2):
        """Concatenates two strings."""
        return str1 + str2

def main():
    Pyro4.Daemon.serveSimple(
            {
                StringConcatenator: "example.stringconcatenator"
            },
            ns = False, port=9090)

if __name__ == "__main__":
    main()
