package sol

type KeyValuePair struct {
	key   string
	value int
}

type Sol struct {
	items []KeyValuePair
}

func (s *Sol) Read(key string) []int {
	foundItem := s.MoveToTop(key)
	if foundItem != nil {
		return []int{foundItem.value}
	}
	return []int{}
}

func (s *Sol) Write(key string, value int) {
	newItem := KeyValuePair{
		key:   key,
		value: value,
	}
	if s.MoveToTop(key) == nil {
		refreshedItems := []KeyValuePair{newItem}
		refreshedItems = append(refreshedItems, s.items...)
		s.items = refreshedItems
		return
	}
	s.items[0] = newItem
}

func (s *Sol) MoveToTop(key string) *KeyValuePair {
	for index, item := range s.items {
		if item.key == key {
			refreshedItems := []KeyValuePair{item}
			refreshedItems = append(refreshedItems, s.items[:index]...)
			refreshedItems = append(refreshedItems, s.items[index+1:]...)
			s.items = refreshedItems
			return &item
		}
	}
	return nil
}
