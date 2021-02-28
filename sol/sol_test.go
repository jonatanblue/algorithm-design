package sol

import (
	"reflect"
	"testing"
)

func TestRead(t *testing.T) {
	expectedReadValue := 200
	sol := Sol{}
	sol.items = []KeyValuePair{
		{key: "a", value: 100},
		{key: "b", value: 200},
		{key: "c", value: 300},
	}
	readValues := sol.Read("b")

	length := len(readValues)
	if length != 1 {
		t.Errorf("readValues is of length %v, want 1", length)
	}

	readValue := readValues[0]
	if readValue != expectedReadValue {
		t.Errorf("got %v, want %v", readValue, expectedReadValue)
	}

	expected := []KeyValuePair{
		{"b", 200},
		{"a", 100},
		{"c", 300},
	}
	actualItems := sol.items
	if !reflect.DeepEqual(actualItems, expected) {
		t.Errorf("got %v, want %v", actualItems, expected)
	}
}

func TestWrite(t *testing.T) {
	sol := Sol{}
	sol.items = []KeyValuePair{
		{key: "a", value: 100},
		{key: "b", value: 200},
		{key: "c", value: 300},
	}

	sol.Write("d", 400)

	expectedItems := []KeyValuePair{
		{"d", 400},
		{"a", 100},
		{"b", 200},
		{"c", 300},
	}
	actualItems := sol.items
	if !reflect.DeepEqual(actualItems, expectedItems) {
		t.Errorf("got %v, want %v", actualItems, expectedItems)
	}
}

func TestOverwriteExistingKey(t *testing.T) {
	sol := Sol{}
	sol.items = []KeyValuePair{
		{key: "a", value: 100},
		{key: "b", value: 200},
		{key: "c", value: 299},
	}

	sol.Write("c", 300)

	expectedItems := []KeyValuePair{
		{"c", 300},
		{"a", 100},
		{"b", 200},
	}
	actualItems := sol.items
	if !reflect.DeepEqual(actualItems, expectedItems) {
		t.Errorf("got %v, want %v", actualItems, expectedItems)
	}
}
