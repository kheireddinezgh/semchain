// SPDX-License-Identifier: GPL-3.0
pragma solidity >=0.7.0 <0.9.0;
import './Registration.sol';
contract Discovery {
    address public owner;
    string[] resource_list = new string[](10);
    Registration registration = new Registration();

    constructor() {
        owner = msg.sender;
    }

    function compare(string memory str1, string memory str2) internal pure returns(bool) {
        return keccak256(abi.encodePacked(str1)) == keccak256(abi.encodePacked(str2));
    }

    function matchmaking(string memory core_link_format_src, string memory core_link_format_dest) internal pure returns(bool) {
        return compare(core_link_format_src, core_link_format_dest);
    }

    function discoverResource_DRDBC(address drd, string memory core_link_format_request) public returns(string[] memory) {
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
                if(matchmaking(resources[j].core_link_format, core_link_format_request) && src_index<src_length) {
                    resource_list[src_index] = resources[j].uri;
                    src_index++;
                }
            }
        }
        return resource_list;
    }

    function discoverResource_DRDH(address drd, string[] memory core_link_formats) public returns(string[] memory) {
        uint devicesLength = registration.devices_count();
        uint resourceLength = 0;
        uint clfLength = core_link_formats.length;
        address[] memory devices = registration.getDrdDevices(drd);
        SharedStructs.Resource[] memory resources;
        uint src_index = 0;
        uint src_length = resource_list.length;
        for(uint k=0; k<clfLength; k++){
            for (uint i=0; i<devicesLength; i++) {
                resources = registration.getDeviceResources(devices[i]);
                resourceLength = resources.length;
                for(uint j=0; j<resourceLength; j++) {
                    if(compare(resources[j].core_link_format, registration.bytes32ToString(keccak256(abi.encode(core_link_formats[k])))) && src_index<src_length) {
                        resource_list[src_index] = resources[j].uri;
                        src_index++;
                    }
                }
            }
        }
        return resource_list;
    }

}