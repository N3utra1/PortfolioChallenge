#include <iostream>
#include <iostream>
#include <SFML/Network.hpp>
#include <string>

using namespace std;

bool checkPort(const std::string& address, int port)
{
    sf::TcpSocket socket;
    bool open = (socket.connect(sf::IpAddress(address), port) == sf::Socket::Done);
    socket.disconnect();
    return open;
}


int main(int argc, char *argv[]) {
    int max = (int)(*argv[0]);
    for(int i = 0; i < max; i++){
        printf("Checking port %d: ", i);
        if(checkPort("localhost", i) == true){
           printf("OPEN\n");
        }else{
           printf("CLOSED\n");
        }
    }
    return 0;
}
