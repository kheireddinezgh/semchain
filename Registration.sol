pragma solidity >=0.7.0 <0.9.0;


library SharedStructs {
    struct Resource {
        string uri;
        string core_link_format;
        string resource_type;
    }
}

contract Registration {
    address public owner;

    mapping(address => address[]) public drds;
    uint public devices_count = 0;
    mapping(address => SharedStructs.Resource[]) public resources;

    constructor() {
        owner = msg.sender;
    }

    function bytes32ToString(bytes32 _bytes32) public pure returns (string memory) {
        uint8 i = 0;
        while(i < 32 && _bytes32[i] != 0) {
            i++;
        }
        bytes memory bytesArray = new bytes(i);
        for (i = 0; i < 32 && _bytes32[i] != 0; i++) {
            bytesArray[i] = _bytes32[i];
        }
        return string(bytesArray);
    }

    function getDeviceResources(address device) public view returns (SharedStructs.Resource[] memory) {
        return resources[device];
    }

    function getDrdDevices(address drd) public view returns (address[] memory) {
        return drds[drd];
    }

    function registerResource_SemChainFull(address device, address drd_owner, string memory core_link_format, string memory uri, string memory resource_type) public {
        drds[drd_owner].push(device);
        devices_count++;
        resources[device].push(SharedStructs.Resource(uri, core_link_format, resource_type));
    }

    function registerResource_SemChainHash(address device, address drd_owner, string memory core_link_format, string memory uri) public {
        //hash CoRE Link Format description
        core_link_format = bytes32ToString(keccak256(abi.encode(core_link_format)));
        drds[drd_owner].push(device);
        devices_count++;
        resources[device].push(SharedStructs.Resource(uri, core_link_format));
    }

}