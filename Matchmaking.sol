pragma solidity >=0.7.0 <0.9.0;
contract Matchmaking {
    address public owner;
    string[] resource_list = new string[](10);

    constructor() {
        owner = msg.sender;
    }

    function compare(string memory str1, string memory str2) internal pure returns(bool) {
        return keccak256(abi.encodePacked(str1)) == keccak256(abi.encodePacked(str2));
    }

    function match(address drd, string memory request_resource_type) public returns(string[] memory) {
        uint devicesLength = registration.devices_count();
        uint resourceLength = 0;
        address[] memory devices = registration.getDrdDevices(drd);
        SharedStructs.Resource[] memory resources;
        uint src_index = 0;
        uint src_length = resource_list.length;
        for (uint i=0; i<devicesLength; i++) {
            resources = registration.getDeviceResources(devices[i]);
            resourceLength = resources.length;
            for(uint j=0; j<resourceLength; j++) {
                if(compare(resources[j].resource_type, request_resource_type) && src_index<src_length) {
                    resource_list[src_index] = resources[j];
                    src_index++;
                }
            }
        }
        return resource_list;
    }
}